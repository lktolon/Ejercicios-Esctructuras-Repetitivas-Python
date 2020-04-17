while True:
    
    print("Seleccione una opción:")
    print("   1. Cómics")
    print("   2. Música")
    print("   3. Videojuegos")
    print("   4. Salir")
    
   
    opcion = int(input("Elija una opción (1-4): "))
   
    if opcion == 1:
        

        print(" .-Saga: My Hero Academia (Boku no Hero Academia) - Kohei Horikoshi")
        print(" .-Saga: Dragon Ball - Akira Toriyama")
        print(" .-Saga: Dead Dead Demons Dededede Destruction - Inio Asano")
    
    elif opcion == 2:
        
        print(" .-The Dark Side of the Moon - Pink Floyd")
        print(" .-Dookie - Green Day")
        print(" .-Nevermind the Bollocks here´s the Sex Pistols - Sex Pistols")
    
    elif opcion == 3:
        
        print(" .-League of Legends (2009) - Riot")
        print(" .-Grand Theft Auto V (2013) - Rockstar Games")
        print(" .-Minecraft (2009) - Mojang AB")
    
    elif opcion == 4:
        
        print("Hasta pronto")
        break;

    else:
        
        print("La opción seleccionada es incorrecta")
