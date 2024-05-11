import os.path
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import get_object_or_404
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .dbhelper import dbCommon
from django.shortcuts import render, redirect
from . import forms


def file_list_view(request):
    try:
        files_list = forms.UploadedFile.objects.all()
        # Phân trang
        items_per_page = 20
        paginator = Paginator(files_list, items_per_page)
        page = request.GET.get('page')
        try:
            files = paginator.page(page)
        except PageNotAnInteger:
            files = paginator.page(1)
        except EmptyPage:
            files = paginator.page(paginator.num_pages)
        return render(request, 'myapp/file_list.html', {'files': files})
    except Exception as e:
        print(e)
        return HttpResponseBadRequest("Bad Request Message")


def upload_file_view(request):
    try:
        if request.method == 'POST':
            fm = forms.UploadFileForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect('file_list')
        else:
            fm = forms.UploadFileForm()
        return render(request, 'myapp/upload_file.html', {'form': fm})
    except Exception as e:
        print(e)
        return HttpResponseBadRequest("Bad Request Message")


class DownloadFileView(View):
    def get(self, request, file_id):
        file = get_object_or_404(forms.UploadedFile, pk=file_id)
        response = HttpResponse(file.file, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={file.filename()}'
        return response


class DeleteFileView(View):
    def get(self, request, file_id):
        file = get_object_or_404(forms.UploadedFile, pk=file_id)

        if os.path.exists(file.file.path):
            os.remove(file.file.path)

        file.delete()
        return redirect('file_list')

