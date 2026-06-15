pe == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                reset()

            if event.key == pygame.K_UP and y_osa == 0:
                x_osa = 0
                y_osa = -blok

            elif event.key == pygame.K_DOWN and y_osa == 0:
                x_osa = 0
                y_osa = blok

            elif event.key == pygame.K_LEFT and x_osa == 0:
                x_osa = -blok
                y_osa = 0

            elif event.key == pygame.K_RIGHT and x_osa == 0:
                x_osa = blok
                y_osa = 0


    if not kraj_igre:

        hx = zmijica[0][0] + x_osa
        hy = zmijica[0][1] + y_osa

        nova = (hx, hy)

        if hx < 0 or hx >= sirina or hy < 0 or hy >= visina:
            kraj_igre = True

        elif nova in zidovi:
            kraj_igre = True

        elif nova in zmijica:
            kraj_igre = True

        else:
            zmijica.insert(0, nova)

            if nova == hrana:

                score += 1

                if score % 5 == 0 and trenutni_level < len(leveli) - 1:

                    trenutni_level += 1

                    tranzicija(trenutni_level + 1)

                    zidovi = napravi_zidove(leveli[trenutni_level]["map"])

                    zmijica = kreiraj_zmijicu()

                    x_osa = blok
                    y_osa = 0

                hrana = kreiraj_hranu(zmijica, zidovi)

            else:
                zmijica.pop()


    screen.fill(crna)

    for z in zidovi:
        pygame.draw.rect(screen, zid_boja, (z[0], z[1], blok, blok), border_radius=4)
        pygame.draw.rect(screen, zid_border, (z[0], z[1], blok, blok), 2, border_radius=4)

    for d in zmijica:
        pygame.draw.rect(screen, zelena, (d[0], d[1], blok, blok), border_radius=6)

    pygame.draw.rect(screen, tamna_zelena, (zmijica[0][0], zmijica[0][1], blok, blok), border_radius=6)

    pygame.draw.rect(screen, crvena, (hrana[0], hrana[1], blok, blok), border_radius=6)

    tekst = font.render(f"Score: {score}  Level: {trenutni_level+1}", True, bijela)
    screen.blit(tekst, (10, 10))

    if kraj_igre:
        g = font.render("GAME OVER - Press R", True, (255, 0, 0))
        screen.blit(g, (220, 260))

    pygame.display.update()
    clock.tick(leveli[trenutni_level]["speed"])
