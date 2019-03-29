#Template Matching 
import numpy as np
import cv2

class match_Prod:

    def mostra(product):
        print(product , 'existe')


    imagem = ['img0.png', 'img1.png', 'img2.png', 'img3', 'img4', 'img5.png',
             'img6.png', 'img7.png', 'img8', 'img9', 'img10.png', 'img11.png',
             'img12.png', 'img13', 'img14', 'img15.png', 'img16.png', 'img17.png',
             'img18', 'img19', 'img20', 'img21.png', 'img22.png', 'img23', 'img24', 
             'img25.png', 'img26.png', 'img27.png', 'img28', 'img29', 'img30.png',
             'img31.png', 'img32.png','img33', 'img34', 'img35', 'img36.png', 'img37.png',
             'img38', 'img39', 'img40.png', 'img41.png', 'img42.png', 'img43', 'img44', 
             'img45.png', 'img46.png', 'img47.png', 'img48', 'img49', 'img50']

    item = ['refrigerante.png','lanche15.png', 'lanche30.png']
    

    #Ler a imagen principal e template
    img_rgb = cv2.imread(imagem[0])
    template0 = cv2.imread(item[0],0)
    template1 = cv2.imread(item[1],0)
    template2 = cv2.imread(item[2],0)
    #Converter 
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    #largura e altura do template w,h
    w, h = template0.shape[::-1] 
    w, h = template1.shape[::-1] 
    w, h = template2.shape[::-1] 
    #verificar match (analise qual eh melhor metodo)
    #res = cv2.matchTemplate(img_gray,template, cv2.TM_CCOEFF)
    res = cv2.matchTemplate(img_gray,template0, cv2.TM_CCOEFF_NORMED)
    res = cv2.matchTemplate(img_gray,template1, cv2.TM_CCOEFF_NORMED)
    res = cv2.matchTemplate(img_gray,template2, cv2.TM_CCOEFF_NORMED)
    #res = cv2.matchTemplate(img_gray,template, cv2.TM_SQDIFF)
    #res = cv2.matchTemplate(img_gray,template, cv2.TM_SQDIFF_NORMED)


    #Especificar um limite (threshold)
    threshold = 0.7

    #array numpy para area conscidente
    loc = np.where( res >= threshold)
    #desenhar retangulo para area encontrada
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)
   
    print('Produtos encontrados \n')
    for i in item:
       # if(item[i] == 'refrigerante.png')
        mostra(' {}'.format(i))

    #Imagem final com area conscidente encontrado
    cv2.imshow('Produto detectado: ',img_rgb)
    #cv2.imwrite('refri_detectado',img_rgb)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
