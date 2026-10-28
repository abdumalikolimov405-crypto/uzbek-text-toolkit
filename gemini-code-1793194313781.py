from uzbek_toolkit import to_cyrillic, validate_uz_phone

print(to_cyrillic("Salom O'zbekiston!"))  # Салом Ўзбекистон!
print(validate_uz_phone("+998 90 123 45 67"))  # True