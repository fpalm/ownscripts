def GravForce( mass1, mass2, distance): # Kopf der Funktion
    GRAV_CONST = 6.673e-11  # Gravitationskonstante  m^3 / ( kg s^2 )
    f = GRAV_CONST * mass1 * mass2 / distance**2 # Kraft ausrechnen
    return(f)                           # Ergebnis zurueckgeben

mSonne= 1.9889e30; mErde = 5.974e24; dErdeSonne = 1.49597e11; rErde = 6.378e6

# Aufruf von Funktion GravForce 
gErdeSonne = GravForce( mSonne, mErde, dErdeSonne ) # Kraft Sonne--Erde
print gErdeSonne
gPerson = GravForce( mErde, 80., rErde )            # Gewichtskraft 80 kg auf Erde
print gPerson
