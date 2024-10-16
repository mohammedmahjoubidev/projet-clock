import tkinter as tk
import time

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Digital Clock")

# تحديد حجم النافذة
root.geometry("300x100")

# إنشاء label لعرض الوقت
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(anchor='center')

# تحديث الوقت كل ثانية
def update_time():
    current_time = time.strftime('%H:%M:%S')  # الحصول على الوقت الحالي
    clock_label.config(text=current_time)  # تحديث الـ label
    clock_label.after(1000, update_time)  # إعادة التحديث كل 1000 مللي ثانية (1 ثانية)

# استدعاء وظيفة تحديث الوقت
update_time()

# بدء الحلقة الرئيسية لتطبيق tkinter
root.mainloop()
