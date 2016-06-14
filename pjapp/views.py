from django.shortcuts import render,redirect
from django.http import HttpResponse
import matplotlib.pyplot as plt
from hellopweb.settings import  BASE_DIR
import os
from django.views.decorators.csrf import csrf_exempt
from cStringIO import StringIO
from django.core.files import File
# Create your views here.

def Hi(request):
    return HttpResponse("<h1>test function ! </h1>")

@csrf_exempt
def latex_func(request):
    if request.method == "GET":
        r_html = request.GET.get('test','')

        im_byte = render_latex(r_html)
        im_path = os.path.join(BASE_DIR, 'static', 'img', 'formu.svg')
        with open(im_path, 'wb') as image_file:
            IMF = File(image_file)
            IMF.write(im_byte)
            image_file.close()

        return HttpResponse("success")

@csrf_exempt
def render_latex(formula, font_size=10, dpi=80, format_='svg'):
    """Renders LaTeX formula into image.
    """
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, u'${}$'.format(formula), fontsize=font_size)
    buffer_ = StringIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_, bbox_inches='tight', pad_inches=0.04)
    plt.close(fig)
    return buffer_.getvalue()

if __name__ == '__main__':
    image_bytes = render_latex(
        r'\theta=\theta+C(1+\theta-\beta)\sqrt{1-\theta}succ_mul',
        fontsize=10, dpi=200, format_='jpg')
    path_f = os.path.join(BASE_DIR,'static','img','formu.jpg')