#6434461423 Phichaphop Raqsaboon 2
def Key_sort(tuple) :
    return tuple[1]
province_list = input("Provinces: ").split(" ")
pattien_list = []
province_pattien_pair = []
for i in province_list :
    pattiens = int(input(f"patients in {i}"))
    pattien_list.append(pattiens)
for i in range(len(province_list)):
    tem_tuple = (province_list[i],pattien_list[i])
    province_pattien_pair.append(tem_tuple)
province_pattien_pair.sort(key=Key_sort , reverse=True)
print("Number of patients: ")
for i in range(0, len(province_pattien_pair)):
    print(f"{province_pattien_pair[i][0]} {province_pattien_pair[i][1]}")