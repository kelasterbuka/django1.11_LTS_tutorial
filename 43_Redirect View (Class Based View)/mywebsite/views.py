from django.views.generic.base import RedirectView,TemplateView


class HomeView(RedirectView):
	# url = '/'
	pattern_name='index'


class HomeUserView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		print(kwargs)
		if self.request.GET.__contains__('tipe'):
			kwargs['tipe'] = self.request.GET['tipe']
		print(kwargs)
		context = kwargs
		return context
		# return super().get_context_data(*args, **kwargs)


# inheritance hanya dari base view
class HomeRedirectView(RedirectView):
	pattern_name='user'
	permanent = False
	query_string = True

	def get_redirect_url(self, *args, **kwargs):
		print(kwargs)
		if kwargs['user'] == 'pukis':
			print('merubah data')
			kwargs['user'] = 'faqihza'
		print(kwargs)
		return super().get_redirect_url(*args, **kwargs)

