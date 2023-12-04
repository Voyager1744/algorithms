"""
Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов:
+7<код><номер>, 8<код><номер>, <номер>, где <номер> — это семь цифр, а <код> — это три цифры или
три цифры в круглых скобках. Если код не указан, то считается, что он равен 495. Кроме того, в
записи телефонного номера может стоять знак “-” между любыми двумя цифрами (см. пример).
На данный момент в адресной книге телефона Васи записано всего три телефонных номера,
и он хочет записать туда еще один. Но он не может понять, не записан ли уже такой номер в
телефонной книге. Помогите ему! Два телефонных номера совпадают, если у них равны коды и равны
номера. Например, +7(916)0123456 и 89160123456 — это один и тот же номер.
"""


def clean_phone(phone):
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace("-", "")

    if len(phone) == 11:
        kod = phone[1:4]
        number = phone[4:]
    elif len(phone) == 12:
        kod = phone[2:5]
        number = phone[5:]
    elif len(phone) == 7:
        kod = "495"
        number = phone
    return kod, number


def equal(phone1, phone2):
    kod1, number1 = clean_phone(phone1)
    kod2, number2 = clean_phone(phone2)
    return kod1 == kod2 and number1 == number2


phone1 = input()
for _ in range(3):
    phone2 = input()
    if equal(phone1, phone2):
        print("YES")
    else:
        print("NO")
