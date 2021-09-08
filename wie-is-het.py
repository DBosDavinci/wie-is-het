geel = input("Is de kaas geel?")

# Is de kaas geel?
if geel == "ja":
    gaten = input("Zitten er gaten in?")
elif geel == "nee":
    schimmels = input("Heeft de kaas blauwe schimmels?")
else:
    print("alleen met ja of nee antwoorden")

# Zitten er gaten in?
if gaten == "ja":
    duur = input("Is de kaas belachelijk duur?")
elif gaten == "nee":
    hard = input("Is de kaas hard als steen?")
else:
    print("alleen met ja of nee antwoorden")

# Is de kaas belachelijk duur?
if duur == "ja":
    print("Emmenthaler")
elif duur == "nee":
    print("Leerdammer")
else:
    print("alleen met ja of nee antwoorden")

# Is de kaas hard als steen?
if hard == "ja":
    print("Parmigiano reggiano")
elif hard == "nee":
    print("Goudse kaas")
else:
    print("alleen met ja of nee antwoorden")

# Heeft de kaas blauwe schimmels?
if schimmels == "ja":
    korstschimmels = input("Heeft de kaas een korst?")
elif schimmels == "nee":
    korst = input("Heeft de kaas een korst?")
else:
    print("alleen met ja of nee antwoorden")

# Heeft de kaas een korst (schimmels)
if korstschimmels == "ja":
    print("Camembert")
elif korstschimmels == "ja":
    print("Mozzarella")
else:
    print("alleen met ja of nee antwoorden")

# Heeft de kaas een korst (zonder schimmels)
if schimmels == "ja":
    print("Bleu de Rochbaron")
elif schimmels == "nee":
    print("Fourme D'Ambert")
else:
    print("alleen met ja of nee antwoorden")