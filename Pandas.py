import pandas as pd 

# laad het Excel-bestand 
bestand= 'jouw_bestand.xlsx' # Vervang dit met de naam van je Excel-bestand
df = pd.read_excel(bestand, engine='openpyxl')

# Controleer op dubbele waarden in kolom 'AV' en voeg een nieuwe kolom 'Dubbel' toe 
df['Dubbel'] = df['AV'].duplicated(keep=false)  # keep=false om alle duplicaten te markeren

# Sla het gewijzigde bestand op 
df.to_excel('jouw_bestand_met_dubbele_waarden.xlsx',index=false, engine='openpyxl')

Print("Script uitgevoerd! De dubbele waarden zijn gemarkeerd")