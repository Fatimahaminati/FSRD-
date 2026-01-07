from website.models import Akademik
for a in Akademik.objects.all():
    print(a.slug)
    print('title:', a.title)
    print('short repr:', repr(a.short))
    print('short len:', len(a.short or ''))
    print('---')
