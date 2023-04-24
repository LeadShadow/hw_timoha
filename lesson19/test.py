import shutil
# zip, tar, gz, gztar


archive_name = shutil.make_archive('backup', 'zip', 'test')
shutil.unpack_archive(archive_name, 'test1')


for shorcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shorcut, description))
