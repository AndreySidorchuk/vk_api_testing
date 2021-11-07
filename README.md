# vk_api_testing
## Запуск
 - Python >= 3.6
 - Для запуска тестов необходимо установить зависимости из requirements.txt
 - Запуск командой `python -m py.test`
## Информация
### В тестах использованы следующие методы vk.api:
1) users_get
2) auth.checkPhone
3) groups.getById
4) groups.isMember

Полную информацию о методах vk.api можно получить по [ссылке](https://vk.com/dev/manuals)

### Дальнейшие планы автоматизации:
- Тестирование изменения наименования и присутсвия в запросах обязательных и необязательных параметров
- Тестирование некорректных значений параметров и их нестандартные значения
