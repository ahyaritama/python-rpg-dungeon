def init():
    return {
        "Gerbang Utama": ["Lorong Barat", "Aula Tengah", "Lorong Timur"],
        "Lorong Barat": ["Gerbang Utama", "Gudang Senjata"],
        "Aula Tengah": ["Gerbang Utama", "Ruang Penjaga", "Perpustakaan Kuno", "Lab Alkemis"],
        "Lorong Timur": ["Gerbang Utama", "Ruang Bawah Tanah"],
        "Gudang Senjata": ["Lorong Barat", "Ruang Penjaga", "Ruang Tahta"],
        "Ruang Penjaga": ["Aula Tengah", "Gudang Senjata"],
        "Perpustakaan Kuno": ["Aula Tengah", "Ruang Tahta"],
        "Lab Alkemis": ["Aula Tengah", "Ruang Jebakan"],
        "Ruang Bawah Tanah": ["Lorong Timur", "Ruang Jebakan"],
        "Ruang Jebakan": ["Lab Alkemis", "Ruang Bawah Tanah"],
        "Ruang Tahta": ["Gudang Senjata", "Perpustakaan Kuno", "Ruang Harta Karun"],
        "Ruang Harta Karun": ["Ruang Tahta"]
    }