if __name__=='__main__':
    from gmeover import callgme
    import pygame
    from pygame import mixer
    # intialize
    pygame.init()
    # game window
    screen = pygame.display.set_mode((800, 600))
    #caption and icon
    pygame.display.set_caption("MARTIAN INVADERS")
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)

    # player
    playerimg = pygame.image.load('player.png')


    def player(xaxis, yaxis):
        # blit means draw, we are drawing player.png on the surface aka on screen #blit(<surface>,(<xcoord>,<ycoord>))
        screen.blit(playerimg, (xaxis, yaxis))
    #music
    mixer.music.load('back.wav')
    mixer.music.play(-1)

    # enemy
    enemyimg = []
    num_of_enemies = 6
    enmX = [float(i) for i in range(0, 326, 65)]
    enmy = []
    enmy_changx = []
    enmy_changey = []
    erender = []
    for i in range(num_of_enemies):
        enemyimg.append(pygame.image.load('enemy.png'))
        enmy.append(0)
        enmy_changx.append(2)
        enmy_changey.append(40)
        erender.append(1)

    renderall=True
    def enemy(enmyx, enmy):
        for i in range(num_of_enemies):
            if erender[i] and renderall:
                screen.blit(enemyimg[i], (enmyx[i], enmy[i]))


    # bullet
    bull_changey = 0
    bullet_img = pygame.image.load('bullet.png')
    bullet_state = 'steady'


    def bullet(bullx, bully):
        global bullet_state
        bullet_state = 'fired'
        if renderall:
            screen.blit(bullet_img, (bullx, bully))


    # Game loop
    xrg = 350
    yarg = 480
    player_changex = 0
    player_changey = 0
    bullx, bully = xrg+27, yarg+6
    running = True
    #score
    score=0
    font= pygame.font.Font('freesansbold.ttf',32)
    def show_score(score,scorex,scorey):
        if renderall:
            score_ren=font.render(f"Score: {score}",True,(255,255,255))
            screen.blit(score_ren,(scorex,scorey))
    show_score(score,10,10)

    tx=font.render(f"GAME OVER YOUR Score is {score}",True,(255,255,255))
    while running:
        if renderall:
            pass
        else:
            running=False
            break
        # background
        screen.fill((0, 0, 0))
        bg = pygame.image.load('space background.png')
        screen.blit(bg, (0, 0))
        #            R  G  B
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if keystroke is pressed tehn check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_changex = -0.96
                if event.key == pygame.K_RIGHT:
                    player_changex = 0.96
                if event.key == pygame.K_UP:
                    player_changey = -0.96
                if event.key == pygame.K_DOWN:
                    player_changey = 0.96
                if event.key == pygame.K_SPACE:
                    a=mixer.Sound("glock.mp3")
                    mixer.Sound.play(a)
                    bullet(xrg, yarg)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_changex = 0
                    player_changey = 0
                    bull_changey = 0
        for i in range(num_of_enemies):
            if renderall:
                if enmy[i]>436:
                    renderall=False
                if enmX[i] <= bullx <= enmX[i]+60 and enmy[i] <= bully <= enmy[i]+60 and renderall:
                    erender[i] = 0
                    score+=10
                    b=mixer.Sound("ror.wav")
                    mixer.Sound.play(b)
                    bullet_state = 'ready'
                # enemy hitting boundary
                enmX[i] += enmy_changx[i]
                if enmX[i] <= 0:
                    enmy_changx[i] = 2
                    enmy[i] += enmy_changey[i]
                elif enmX[i] >= 736:
                    enmy_changx[i] = -2
                    enmy[i] += enmy_changey[i]
        enemy(enmX, enmy)
        # bullet motion
        if bullet_state == 'ready':
            bully = yarg+6
            bullx = xrg+27
        if bullet_state == "fired":
            bull_changey = -0.9
            bully += bull_changey
            bullet(bullx, bully)
            if bully < 0:
                bullet_state = 'ready'
                bull_changey = 0
                bully = yarg+6
                bullx = xrg+27
        if (xrg > 735):
            xrg = 734
            player_changex = 0
        if (xrg < 1):
            xrg = 2
            player_changex = 0
        if(yarg > 535):
            yarg = 534
            player_changey = 0
        elif yarg < 0:
            yarg = 1
            player_changey = 0

        xrg += player_changex
        yarg += player_changey
        player(xrg, yarg)
        show_score(score,10,10)
        # screen update
        pygame.display.update()
    if running==False:
        # import mysql.connector as c
        # con=c.connect(host='localhost',user='root',password='',database='game')
        # if con.is_connected():
        #    print('successfully connected')
        # else:
        #    print('not connected')
        # curso=con.cursor()
        # sql='delete table if exists invaders'
        # curso.commit(sql)
        # sql="create table gamers(score integer)"
        # curso.commit(sql)
        # sql=f'insert into gamers values({score})'
        # curso.commit(sql)
        callgme()