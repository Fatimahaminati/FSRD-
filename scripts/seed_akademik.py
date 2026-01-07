from website.models import Akademik

data = [
    {
        'title': 'Program Sarjana',
        'slug': 'sarjana',
        'short': 'Fakultas Seni Rupa dan Desain (FSRD) Universitas Muhammadiyah Surakarta (UMS) menyelenggarakan pendidikan jenjang Sarjana (S1) melalui beberapa program studi, yaitu Program Studi Seni Rupa dan Program Studi Desain Komunikasi Visual (DKV).',
        'full': 'Fakultas Seni Rupa dan Desain (FSRD) Universitas Muhammadiyah Surakarta (UMS) menyelenggarakan pendidikan jenjang Sarjana (S1) melalui beberapa program studi, yaitu Program Studi Seni Rupa dan Program Studi Desain Komunikasi Visual (DKV).'
    },
    {
        'title': 'Program PascaSarjana',
        'slug': 'pasca-sarjana',
        'short': 'Untuk jenjang Pascasarjana, Fakultas Seni Rupa dan Desain Universitas Muhammadiyah Surakarta menyelenggarakan Program Studi Magister Seni Rupa dan Desain.',
        'full': 'Untuk jenjang Pascasarjana, Fakultas Seni Rupa dan Desain Universitas Muhammadiyah Surakarta menyelenggarakan Program Studi Magister Seni Rupa dan Desain.'
    },
    {
        'title': 'Beasiswa',
        'slug': 'beasiswa',
        'short': 'FSRD UMS menyediakan berbagai program beasiswa bagi mahasiswa jenjang Sarjana dan Pascasarjana sebagai bentuk komitmen dalam mendukung akses pendidikan yang inklusif dan berkeadilan.',
        'full': 'FSRD UMS menyediakan berbagai program beasiswa bagi mahasiswa jenjang Sarjana dan Pascasarjana sebagai bentuk komitmen dalam mendukung akses pendidikan yang inklusif dan berkeadilan.\n\nProgram beasiswa yang tersedia meliputi beasiswa internal Universitas Muhammadiyah Surakarta, beasiswa dari pemerintah, serta beasiswa dari mitra dan lembaga eksternal, yang diberikan berdasarkan prestasi akademik, non-akademik, maupun kondisi ekonomi mahasiswa.'
    }
]

for it in data:
    obj, created = Akademik.objects.update_or_create(
        slug=it['slug'],
        defaults={'title': it['title'], 'short': it['short'], 'full': it['full']}
    )
    print(obj.slug + (' created' if created else ' updated'))
