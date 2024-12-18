from pddiktipy import api

a = api()

nama_kampus = "INSTITUT TEKNOLOGI KALIMANTAN" # Ubah sesuai kampus yang ingin di scapping 

for angkatan in range (18,24):
    isFound = True
    modified = 1 
    output_file = f"data_if{angkatan}.txt" 

    with open(output_file, "w") as file:
        file.write("Nama\tNIM\n")

        while isFound:
            nim = f"11{angkatan}10{modified:02d}" # Pola NIM bisa disesuaikan
            try:
                result = a.search_all(nim)
                if result and 'mahasiswa' in result and result['mahasiswa']:
                    filtered_results = [
                        student for student in result['mahasiswa']
                        if student['nim'] == nim and student['nama_pt'] == nama_kampus
                    ]
                    if filtered_results:
                        for student in filtered_results:
                            file.write(f"{student['nama']}\t{student['nim']}\n")
                        print(f"{student['nama']}\t{student['nim']}")
                    else:
                        if modified == 130:
                            isFound = False  
                else:
                    print("No students found or unexpected response.")
                    isFound = False  
            except Exception as e:
                print(f"Error fetching data: {e}")
                isFound = False  
            
            modified += 1
