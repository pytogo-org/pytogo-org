from datetime import datetime, timezone

# La date à convertir
date_str = "25 March 2025 17:00 GMT"

# Parser la date
date_obj = datetime.strptime(date_str, "%d %B %Y %H:%M %Z")

date_obj = date_obj.replace(tzinfo=timezone.utc)

# Vérification
print("Date convertie:", date_obj)

date_obj = datetime(2025, 3, 9).replace(tzinfo=timezone.utc)


# Date actuelle en UTC
now = datetime.now(timezone.utc)


print("Date actuelle:", now)

# Comparaison
if date_obj > now:
    print("La date est dans le futur.")
elif date_obj < now:
    print("La date est dans le passé.")
else:
    print("C'est maintenant !")
