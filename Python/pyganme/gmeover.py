# def load_score():
#     import mysql.connector as c
#     con=c.connect(host='localhost',user='root',password='',database='game')
#     if con.is_connected():
#        print('successfully connected')
#     else:
#        print('not connected')
#     curso=con.cursor()
#     sql='select * from invaders'
#     curso.commit(sql)
#     dat=curso.fetchall()
#     return dat
#     This is commented until mysql
    
def callgme():
    import pygame 
    from pygame import mixer
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("SCORE BOARD")
    icon= pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    mixer.music.load('ProjectTFS.wav')
    mixer.music.play()
    running=True
    font=pygame.font.Font('freesansbold.ttf',32)
    while running:
        screen.fill((0,0,0))
        # score=load_score()
        score = 2
        #until mysql
        score_render=font.render(f"GAME OVER YOUR SCORE IS : {score}",True,(255,255,255))
        for evnt in pygame.event.get():
            if evnt.type==pygame.QUIT:
                running=False
        screen.blit(score_render,(150,250))
        pygame.display.update()
# if __name__=='__main__':
    callgme()