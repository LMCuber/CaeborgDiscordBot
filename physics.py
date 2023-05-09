formulas = {
        # Example:
        # "name": (
        #         "formule",
        #         ("needed", "other", "variables")
        # ),
        
        "eenparige_beweging": (
                "s = v·t",
                ("s = afgelegde weg (m)", "v = snelheid (m/s)", "t = tijd (s)")
        ),
    
        "gemiddelde_snelheid": (
                "vgem = Δx/Δt",
                ("vgem = gemiddelde snelheid (m/s)", "Δx = verplaatsing (m)", "Δt = tijdsduur (s)")
		),
        "eenparige_versnelde_beweging": (
                "s = ½a·t2",
                ("s = afgelegde weg (m)", "a = versnelling (m/s2)", "t = tijd (s)")
		),
        "versnelling": (
                "a = Δv / Δt",
                ("a = versnelling (m/s2)", "Δv = snelheidsverandering (m/s)", "Δt = tijdsduur (s)")
		),
        "baansnelheid": (
                "vbaan = 2π·r / T",
                ("vbaan = baansnelheid (m/s)", "r = straal (m)", "T = omlooptijd (s)")
		),
        "hoeksnelheid": (
                "ω = 2π / T",
                ("ω = hoeksnelheid (rad/s)", "T = omlooptijd (s)")
		),
        "middelpuntzoekende_kracht": (
                "Fmpz = mv2/r",
                ("Fmpz = middelpuntzoekende kracht (N)", "m = massa (kg)", "v = baansnelheid (m/s)", "r = straal (m)")
		),
        "resulterende_kracht": (
                "Fres = Σ Fi",
                ("Fres = somkracht (N)", "F1,2,3… = deelkrachten (N)")
		),
        "ontbinden": (
                "FA = F·sin αFB = F·cos α",
                ("F = kracht (N)", "FA = ene component (N)", "FB = andere component (N)")
		),
        "1e_wet_van_Newton": (
                "ΣF=0 ⇔ v=constant",
                ("ΣF = nettokracht (N)", "v = snelheid (m/s)")
		),
        "2e_wet_van_Newton": (
                "ΣF = m·a",
                ("ΣF = nettokracht (N)", "m = massa (kg)", "a = versnelling (m/s2)")
		),
        "3e_wet_van_Newton": (
                "FA→B = -FB→A",
                ("FA→B kracht A op B (N)", "FB→A kracht van B op A (N)")
		),
        
        "zwaartekracht": (
                "Fz = m·g",
                ("Fz = zwaartekracht (N)", "m = massa (kg)", "g = 9,81 m/s2 (op aarde)")
        ),
        
        "gravitatiekracht": (
                "Fg = G·m1m2 / r2",
                ("Fg = gravitatiekracht (N)", "G = 6,67384·10^-11 (Nm^2kg^-2)", "m1,2 = massa's (kg)", "r = afstand (m)")
        ),
        
        "gravitatie_energie": (
                "Eg = -G·m1m2 / r",
                ("Eg = gravitatie-energie (J)", "G = 6,67384·10^-11 Nm2kg-2", "m1,2 = massa's (kg)", "r = afstand (m)")
        ),

        "3e_wet_van_Kepler": (
                "r^3/T^2 = G·M / 4π^2",
                ("r = baanstraal (m)", "T = omlooptijd (s)", "G = 6,67384·10^-11 Nm2kg-2", "M = centrale massa (kg)")
        ),

        "veerkracht":  (
                "Fv = C·u",
                ("Fv = veerkracht (N)", "C = veerconstante (Nm^-1)", "u = uitrekking (m)")
        ),
        
        "luchtweerstand": (
		        "Fw,l = ½ ρ CW A v2",
                ("Fw,l = luchtwrijving (N)", "ρ = luchtdichtheid (kg/m3)", "CW = weerstandscoefficient", "A = oppervlak (m2)", "v = snelheid (m/s)")
		),
        
        "schuifwrijving": (
		        "Fs,max = f · FN",
                ("Fs,max = max. schuifwrijving (N)", "f = constante", "FN = normaalkracht (N)")
		),
        
        "arbeid": (
		        "W = F·s (·cos α)",
                ("W = arbeid (J)", "F = kracht (N)", "s = afgelegde weg (m)", "(α = hoek tussen F en s)")
		),
        
        "vermogen": (
		        "P = E/t\nP = W/t",
                ("P = vermogen (Js-1 of W)", "E = energie (J)", "W = arbeid (J)", "t = tijd (s)")
		),
        
        "bewegend_voorwerp": (
		        "P = F·v",
                ("P = vermogen (Js-1 of W)", "F = kracht (N)", "v = snelheid (ms-1)")
		),
        
        "kinetische_energie": (
		        "Ek = ½m·v2",
                ("Ek = kinetische energie (J)", "m = massa (kg)", "v = snelheid (m/s)")
		),
        
        "zwaarte-energie": (
		        "Ez = m·g·h",
                ("Ez = zwaarte-energie (J)", "m = massa (kg)", "g = 9,81 m/s2 (op aarde)", "h = hoogte (m)")
		),
        
        "veerenergie": (
		        "Ev = ½C·u2",
                ("Ev = veerenergie (J)", "C = veerconstante (N/m)", "u = uitrekking (m)")
		),
        
        "chemische_energie": (
		        "Ech = rV·V\nEch = rm·m",
                ("Ech = chemische energie (J)", "rV,m = stookwaarde (J/m3 of J/kg)", "V = volume (m3)", "m = massa (kg)")
		),
        
        "rendement": (
			    "η = Enuttig / Everbruikt\nη = Pnuttig / Pverbruikt",
                ("η = rendement", "Enuttig = nuttig gebruikte energie (J)", "Everbruikt = verbruikte energie (J)", "Pnuttig = nuttig vermogen (W)", "Pverbruikt = verbruikt vermogen (W)")
		),
        
        "wet_van_behoud_van_energie": (
		        "Σ Evoor = Σ Ena",
                ("Σ Evoor = beginenergie (J)", "Σ Ena = eindenergie (J)")
        ),

        "ontsnappingssnelheid": (
                "v_ontsn = √(2 GM/r)",
                ("vontsn = ontsnappingssnelheid (m/s)", "G = 6,67384·10^-11 Nm^2kg^-2", "M = massa planeet (kg)", "r = straal planeet (m)")
        )
        
        "rek": (
                "ε = ΔL/L0",
                ("ε = rek", "ΔL = uitrekking (m)", "L0 = beginlengte (m)")
        ),
        
        "spanning_mechanisch": (
                "σ = F/A",
                ("σ = spanning (N/m2)", "F = kracht (N)", "A = doorsnede (m2)")
        ),
        
        "elasticiteit": (
                "E = σ/ε",
                ("E = elasticiteit (N/m2)", "σ = spanning (N/m2)", "ε = rek")
        ),
        
        "moment": (
                "M = F·r",
                ("M = moment (Nm)", "F = kracht (N)", "r = arm (m)")
        ),
        
        "hefboomwet": (
                "F1·r1 = F2·r2",
                ("F1,2 = kracht (N)", "r1,2 = arm (m)")
        ),
        
        "frequentie": (
                "f = 1/T",
                ("f = frequentie (Hz)", "T = trillingstijd (s)")
        ),
        
        "faseverschil_bij_trilling": (
                "Δφ = Δt/T",
                ("Δφ = faseverschil", "Δt = tijdsverschil (s)", "T = trillingstijd (s)")
        ),
        
        "harmonische_trilling_uitwijking": (
                "u = A sin (2π·f·t)",
                ("u = uitwijking (m)", "A = amplitude (m)", "f = frequentie (Hz)", "t = tijd (s)")
        ),
        
        "harmonische_trilling_kracht": (
                "F = -C·u",
                ("-C = constante (N/m)", "F = kracht (N)", "u = uitwijking (m)")
        ),
        
        "maximale_snelheid_harmonische_trilling": (
                "vmax = 2πA/T",
                ("vmax = maximale snelheid (m/s)", "A = amplitude (m)", "T = trillingstijd (s)")
        ),
        
        "massa_veersysteem": (
                "T = 2π·√(m/C)",
                ("T = trillingstijd (s)", "m = massa (kg)", "C = veerconstante (N/m)")
        ),
        
        "slinger": (
                "T = 2π·√(L/g)",
                ("T = trillingstijd (s)", "L = lengte slinger (m)", "g = 9,81 m/s2 (op aarde)")
        ),
        
        "golfsnelheid": (
                "v = f ·λ",
                ("v = golfsnelheid (m/s)", "f = frequentie (Hz)", "λ = golflengte (m)")
        ),
        
        "faseverschil_golf": (
                "Δφ = Δx/ λ", 
                ("Δφ = faseverschil", "Δx = weglengteverschil (m)", "λ = golflengte (m)")
        ),
        
        "lengte_snaar": (
                "L = ½n·λ",
                ("L = lengte snaar (m)", "n = 1,2,3,…", "λ = golflengte (m)")
        ),

        "lengte_open_buis": (
                "L = ½n·λ",
                ("L = lengte snaar (m)", "n = 1,2,3,…", "λ = golflengte (m)")
        ),

        "lengte_enkelgesloten_buis": (
                "L = ¼(2n-1)·λ", 
                ("L = lengte buis (m)", "n = 1,2,3,…", "λ = golflengte (m)")
        ),
        
        "frequentie_snaar": (
                "f = ½n v/L", 
                ("f = frequentie (Hz)", "n = 1,2,3,…", "v = golfsnelheid (m/s)", "L = lengte snaar (m)")
        ),
        
        "frequentie_open_buis": (
                "f = ½n v/L", 
                ("f = frequentie (Hz)", "n = 1,2,3,…", "v = golfsnelheid (m/s)", "L = lengte buis (m)")
        ),
        
        "frequentie_enkelgesloten_buis": (
                "f = ¼(2n-1) v/L", 
                ("f = frequentie (Hz)", "n = 1,2,3,…", "v = golfsnelheid (m/s)", "L = lengte buis (m)")
        ),
        
        "stroomsterkte": (
                "I = Q/t", 
                ("I = stroomsterkte (A)", "Q = lading (C)", "t = tijdsduur (s)")
        ),
        
        "wet_van_ohm": (
                "U = I·R", 
                ("U = spanning (V)", "I = stroomsterkte (A)", "R = weerstand (Ω)")
        ),
        
        "geleidingsvermogen": (
                "G = 1/R", 
                ("G = geleidingsvermogen (S)", "R = weerstand (Ω)")
        ),
        
        "vermogen": (
                "P = U·I", 
                ("P = elektrisch vermogen (W)", "U = spanning (V)", "I = stroomsterkte (A)")
        ),
        
        "energie": (
                "E = P·t", 
                ("E = elektrische energie (J)", "P = elektrisch vermogen (W)", "t = tijdsduur (s)")
        ),
        
        "soortelijke_weerstand": (
                "R = ρ·L/A", 
                ("R = weerstand (Ω)", "ρ = soortelijke weerstand (Ωm)", "L = lengte (m)", "A = oppervlak (m2)")
        ),
        
        "vervangingsweerstand_in_serie": (
                "RV = R1 + R2+…", 
                ("RV = vervangingsweerstand (Ω)", "R1,2,3… = weerstanden (Ω)")
        ),
        
        "vervangingsweerstand_in_parallel": (
                "1/RV = 1/R1+1/R2+…", 
                ("RV = vervangingsweerstand (Ω)", "R1,2,3… = weerstanden (Ω)")
        ),
        
        "stroom_in_serie": (
                "I1 = I2 =I3 = …", 
                ("I1,2,…… = deelstromen (A)",)
        ),
        
        "spanning_in_serie": (
                "Utotaal = U1 + U2 + …", 
                ("Utotaal = totaalspanning (V)", "U1,2,…… = deelspanningen (U)")
        ),

        "stroom_parallel": (
                "I_hoofd = I_1 + I_2 + ...",
                ("I_hoofd = hoofdstroom (A)", "I_1,2 = deelstromen (A)")
        ),

        "spanning_parallel": (
                "U1 = U2 = U3 = …",
                ("U1,2,… = deelspanningen (U)")
        ),
        
        "wet_van_kirchhoff_stroom": (
                "ΣIn = 0",
                ("I1,2,3,… = deelstromen van/naar één punt (A)")
        ),
        
        "wet_van_kirchhoff_spanning": (
                "ΣUn = 0",
                ("U1,2,3,… = deelspanningen in kring (V)")
        ),
        
        "wet_van_coulomb": (
                "Fel = f·Qq/r2",
                ("Fel = kracht(N)", "f = 8,987551787·109 Nm2/C2", "Q,q = ladingen(C)", "r = afstand (m)")
        ),
        
        "veldsterkte": (
                "E = F/q",
                ("E = veldsterkte (N/C)", "F = kracht (N)", "q = lading (C)")
        ),
        
        "elektrische_spanning": (
                "ΔU = ΔEel/q",
                ("ΔU = spanningsverschil (V)", "ΔEel = energieverschil (J)", "q = lading (C)")
        ),
        
        "magnetische_veldsterkte_spoel": (
                "B = μ0·N·I/L",
                ("B = magnetische veldsterkte (T)", "μ0 = 1,256643706·10-6 H/m", "N = aantal wikkelingen", "I = stroomsterkte (A)", "L = spoellengte (m)")
        ),
        
        "lorentzkracht_deeltje": (
                "FL = B·q·v",
                ("FL = lorentzkracht (N)", "B = magnetische veldsterkte (T)", "q = lading (C)", "v = snelheid (m/s)")
        ),
        
        "lorentzkracht_draad": (
                "FL = B·I·L",
                ("FL = lorentzkracht (N)", "B = magnetische veldsterkte (T)", "I =stroomsterkte (A)", "L =draadlengte (m)")
        ),
        
        "flux": (
                "Φ = B·A",
                ("Φ = magnetische flux (Wb)", "B = magnetische veldsterkte (T)", "A = oppervlak (m2)")
        ),
        
        "inductiespanning": (
                "Uind = N·ΔΦ/Δt",
                ("Uind = inductiespanning (V)", "N = aantal windingen", "ΔΦ = fluxverandering (Wb)", "Δt = tijdsduur (s)")
        ),
        
        "wisselspanning_sinusvormig": (
                "Ueff = ½√2·Umax",
                ("Ueff = effectieve spanning (V)", "Umax = maximale spanning (V)")
        ),
        
        "transformator": (
                "Np/Ns = Up/Us = Is/Ip",
                ("Np = primaire windingen", "Ns = secundaire windingen", "Up = primaire spanning (V)", "Us = secundaire spanning (V)", "Ip = primaire stroom (A)", "Is = secundaire stroom (A)"
        ),

        "fotonenergie": (
                "Ef = h·f = h·c/λ",
                ("Efoton = energie per foton (J)", "h = 6,62606957·10-34 Js", "f = frequentie (Hz)", "c = 2,9979·108", "λ = golflengte (m)")
        ),
                
        "overgang": (
                "Ef = |Em-En|",
                ("Ef = fotonenergie (J)", "Em = energieniveau voor (J)", "En = energieniveau na (J)")
        ),
                
        "remspanning": (
                "|q·Urem|= Efoton - Euittree",
                ("q = 1,602176565·10-19 C", "Urem = remspanning (V)", "Efoton = fotonenergie (J)", "Euittree = uittree-energie (J)")
        ),
                
        "energie_waterstofatoom": (
                "En = -13,6 / n2",
                ("En = energie t.o.v. ionisatieniveau (eV)", "n = quantumgetal (1,2,3,…)")
        ),
                
        "de_brogliegolflengte": (
                "λ = h/p = h
                (mv)", ("λ = golflengte deeltje (m)", "h = 6,62606957·10-34 Js", "p = impuls (kg m/s)", "m = massa (kg)", "v = snelheid (m/s)")
        ),
                
        "heisenbergrelatie": (
                "Δx·Δp ≥ h/4π",
                ("Δx = onzekerheid plaats (m)", "Δp = onzekerheid impuls (kg m/s)", "h = 6,62606957·10-34 Js")
        ),
                
        "opgesloten_deeltje": (
                "En = n2h2/8mL2",
                ("En = energie (J)", "n = niveau (1,2,3,…)", "h = 6,62606957·10-34 Js", "m = massa (kg)", "L = breedte put (m)")
        ),
                
        "wet_van_wien": (
                "λmax = kW/T",
                ("λmax = golflengte maximum (m)", "kW = 2,8977721·10-3 mK", "T = temperatuur (K)")
        ),
                
        "dopplereffect": (
                "v = c· Δλ/λ",
                ("v = radiële snelheid (ms-1)", "c = 2,99792458·108 ms-1", "Δλ = golflengteverschuiving (m)", "λ = golflengte (m)")
        ),
                
        "stefan-boltzmann": (
                "Pbron = σAT4",
                ("Pbron = vermogen (W)", "σ = 5,670373·10-8 Wm-2K-4", "A = oppervlakte (m2)", "T = temperatuur (K)")
        ),
                
        "kwadratenwet": (
                "I = Pbron/4πr2",
                ("I = intensiteit (Wm-2)", "Pbron = vermogen (W)", "r = afstand (m)")
        ),

        "wet_van_snellius": (
                "sin i / sin r = nr / ni",
                ("i = invalshoek (graden)", "r = brekingshoek (graden)", "nr = brekingsindex brekingskant", "ni = brekingsindex invalskant")
        )

}
