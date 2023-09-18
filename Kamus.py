meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            'gg': 'Tanggapan kepada sesuatu yang keren',
            'NR': 'No retri',
            'NF': 'No fliker'
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print('Kata itu tidak ada')
