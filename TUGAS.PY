listplatnomor = ('G 2345 AM,G 3456 NO')
plat_nomor = str(input('plat nomor : '))
listnim = ('23090166,2309023,2309066')
NIM = str(input('masukan NIM mahasiswa : '))

print('hasil')
print('plat nomor')
print('nim')

if plat_nomor in listplatnomor and NIM in listnim :
    print('plat nomor :', plat_nomor)
    print('NIM :', NIM)
    print('boleh keluar kampus')
else:
    print('tidak boleh keluar kampus')
