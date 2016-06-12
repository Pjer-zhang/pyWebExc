from django.shortcuts import render
from django.http import HttpResponse
import matplotlib as plt
import os
from django.views.decorators.csrf import csrf_exempt
import StringIO
# Create your views here.

def Hi(request):
    return HttpResponse("<h1>test function ! </h1>")


@csrf_exempt
def latex_func(request):
    if request.method == "POST":
        r_html = request.POST.get('test','')
        print r_html
        return HttpResponse(r_html)
    return HttpResponse("sb")


def render_latex(formula, fontsize=12, dpi=500, format_='svg'):
    """Renders LaTeX formula into image.
    """
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)
    buffer_ = StringIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_, bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)
    return buffer_.getvalue()

if __name__ == '__main__':
    image_bytes = render_latex(
        r'\theta=\theta+C(1+\theta-\beta)\sqrt{1-\theta}succ_mul',
        fontsize=10, dpi=200, format_='jpg')
    with open('src'+os.seq+'formula.png', 'wb') as image_file:
        image_file.write(image_bytes)