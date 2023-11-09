def testing(request):
  template = loader.get_template('template.html')
  context = {
    'mymembers': showdb(),
  }
  return HttpResponse(template.render(context, request))