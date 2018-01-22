string = 'Vm0xd1NtUXlWa1pPVldoVFlUSlNjRlJVVGtOamJGWnhVMjA1VlUxV2NIbFdiVEZIWVZaYWRW RnNhRmRXTTFKUVZrZDRXbVF3TlZsalJsWk9WakZLTmxaclVrZFVNVXB5VFZaV1dHSkhhRlJW YkZwM1ZGWlplVTFVVW1wTmF6VllWbGMxVjFaWFJqWldiRkpoVmpOb2FGUldXbHBrTWtaSldr WlNUbGRGU2paV2FrbzBZekZhV0ZKdVVtcGxiWE01'
result = ''

while(True):
    result = string.decode('base64')
    string = result
    if('flag' in result):
        print result
        break
