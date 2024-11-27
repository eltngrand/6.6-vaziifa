from django.shortcuts import render
from django.contrib import messages
import json

def form_(request):
    if request.method == "POST":
        # POST so'rovidan kelgan ma'lumotlarni olish
        user_data = {
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "address": request.POST.get("address"),
            "address2": request.POST.get("address2"),
            "city": request.POST.get("city"),
            "state": request.POST.get("state"),
        }

        # Bo'sh maydonlarni tekshirish
        missing_fields = [key for key, value in user_data.items() if not value]
        
        if missing_fields:
            # To'ldirilmagan maydonlar haqida xabar ko'rsatish
            messages.error(request, f"Quyidagi maydonlarni to'ldiring: {', '.join(missing_fields)}")
            # Foydalanuvchiga formani qayta render qilish
            return render(request, 'form_app/form.html')

        # JSON faylga yozish
        try:
            # JSON faylni o'qish va mavjud bo'lgan ma'lumotlarni qo'shish
            with open('user_data.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            # Agar fayl yo'q bo'lsa, yangi ro'yxat yaratish
            data = []

        # Yangi ma'lumotlarni ro'yxatga qo'shish
        data.append(user_data)

        # Yangilangan ma'lumotlarni JSON faylga yozish
        with open('user_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        # Muvaffaqiyatli saqlash xabari
        messages.success(request, "Ma'lumotlaringiz muvaffaqiyatli saqlandi")
        return render(request, 'form_app/form.html')

    # GET so'rovi uchun formani ko'rsatish
    return render(request, 'form_app/form.html')
