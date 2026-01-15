# 1. Создайте словарь email, содержащий следующие поля:
# "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).
import datetime
import math

email = {"subject": "Story telling  ",
         "from": "  12345ZionCAMichaelLanda@dot.com ",
         "to": "   8762-Orley-WY-MrSmith@yandex.ru  ",
         "body": "\t Somebody wrote about this story, so that, finally, \n You should do it wright now Jhonny!"}

print(f'Task 1. email: {email} \n')

# 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в
# email["date"].

send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date
print(f'Task 2. email: {email}')
print(f'Task 2. send_date: {send_date} \n')

# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].

email_from_corrected = email['from'].lower().strip()
email_to_corrected = email['to'].lower().strip()
email['from'] = email_from_corrected
email['to'] = email_to_corrected
print(f'Task 3. email_from_corrected: {email_from_corrected}')
print(f'Task 3. email_to_corrected: {email_to_corrected}')
print(f'Task 3. email: {email} \n')

# 4. Извлеките логин и домен отправителя в две переменные login и domain.

from_after_split = email['from'].split('@')
login = from_after_split[0]
domain = from_after_split[1]
print(f'Task 4. login: {login}, domain: {domain} \n')

# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].

short_body = email['body'][0:10]+"..."
email['short_body']= short_body
print(f'Task 5. email: {email} \n')

# 6. Списки доменов: создайте список личных доменов
# ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
# и список корпоративных доменов
# ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']. с учетом того что там должны быть только уникальные значение

private_domain_list = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru',
                       'mail.ru','list.ru','bk.ru','inbox.ru']
corporate_domain_list = ["company.ru","corporation.com","university.edu","organization.org","company.ru","business.net"]
print(f'Task 6. private_domain_list: {private_domain_list}')
print(f'Task 6. corporate_domain_list: {corporate_domain_list}')

reduced_corporate_domain_list = list(set(corporate_domain_list))
print(f'Task 6. reduced_corporate_domain_list: {reduced_corporate_domain_list} \n')

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений: ни один домен не должен входить в оба списка одновременно.

set_1 = set(private_domain_list)
set_2 = set(corporate_domain_list)
var_1 = bool(set_1 & set_2)
var_2 = bool(set_2 & set_1)
print(f'Task 7. Is private_domain_list intersets reduced_corporate_domain_list? {var_1}')
print(f'Task 7. Is reduced_corporate_domain_list intersects private_domain_list? {var_2}\n')

# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки вхождения домена отправителя в список корпоративных доменов.

is_corporate = any(item in corporate_domain_list for item in private_domain_list)
print(f'Task 8. is_corporate: {is_corporate}\n')

# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].

clean_body = email["body"].replace("\n", "").replace("\t", " ").replace("  ", " ")
email["clean_body"] = clean_body
print(f'Task 9. clean_body: {clean_body}')
print(f'Task 9. email: {email} \n')

# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}

sent_text = f'''
Кому: {email['to']},
От: {email['from']}
Тема: {email['subject']},
Дата: {email['date']},
Тест: {email['clean_body']}'''
email['sent_text'] = sent_text
print(f'Task 10. sent_text: {sent_text}\n')
print(f'Task 10. email: {email} \n')

# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.

sent_text_length = len(email['sent_text'])
pages = math.ceil(sent_text_length / 500)
print(f'Task 11. sent_text_length: {sent_text_length}')
print(f'Task 11. pages: {pages} \n')

# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty в котором будет
# храниться что тема письма содержит данные.

is_subject_empty = email['subject'] is None
is_body_empty = email['body'] is None
print(f'Task 12. is_subject_empty: {is_subject_empty}')
print(f'Task 12. is_body_empty: {is_body_empty}\n')

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].

login_first_part = email['from'][:2]
email['masked_from'] = login_first_part+'***'+'@'+domain
print(f'Task 13. from: {email['from']}')
print(f'Task 13. masked_from: {email['masked_from']} \n')

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".

print(f'Task 14. private_domain_list before clearing: {private_domain_list}')
updated_list = list(set(private_domain_list))
updated_list.remove('list.ru' and 'bk.ru')
print(f'Task 14. private_domain_list after clearing: {updated_list}')