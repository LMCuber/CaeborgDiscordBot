formulas = {
        # Example:
        # "name": (
        #         "formule",
        #         ("needed", "other", "variables")
        # ),
        
        "eenparige_beweging": (
                "s = v·t ",
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
		)
}
