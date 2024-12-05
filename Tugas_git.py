data_panen = {
    'lokasi1': {
        'nama_lokasi':'kebun A',
        'hasil_panen': {
            'padi':1200,
            'jagung':800,
            'kedelai':500
        }
    },
    'lokasi2': {
        'nama_lokasi':'kebun B',
        'hasil_panen': {
            'padi':1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'lokasi3': {
        'nama_lokasi':'kebun C',
        'hasil_panen': {
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4': {
        'nama_lokasi':'kebun D',
        'hasil_panen': {
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5': {
        'nama_lokasi':'kebun E',
        'hasil_panen': {
            'padi':1400,
            'jagung':950,
            'kedelai':480
        }
    }
}

for lokasi, data in data_panen.items():
    print(f"nama lokasi:{data['nama_lokasi']}")
    print('hasil_panen:')
    for hasil, jumlah in data['hasil_panen'].items():
        print(f"{hasil}:{jumlah}")
    print()

jumlahJagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"jumlah hasil panen jagung dari lokasi2 adalah: {jumlahJagung_lokasi2}")

namaLokasi_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"nama dari lokasi3 adalah: {namaLokasi_lokasi3}")

jumlah_hasilPadi = []
jumlah_hasilKedelai =[]

for lokasi, data in data_panen.items():
    jumlah_hasilPadi.append(data['hasil_panen']['padi'])
    jumlah_hasilKedelai.append(data['hasil_panen']['kedelai'])

print(jumlah_hasilKedelai)
print(jumlah_hasilPadi)

for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {data['nama_lokasi']} dalam kondisi baik.")

