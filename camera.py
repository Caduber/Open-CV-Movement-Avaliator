import cv2
import numpy as np
import time as time


def fodase():

    # Inicializa a captura de vídeo
    cap = cv2.VideoCapture(0) 

    # Lê o primeiro quadro e converte para escala de cinza
    ret, frame1 = cap.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    score = 0
    count = 0
    movimentos_validos = 0

    while cap.isOpened():
        ret, frame2 = cap.read()
        if not ret:
            break
        
        count += 1
        
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        # Calcula a diferença entre os quadros
        diff = cv2.absdiff(gray1, gray2)
        
        # Aplicar um limiar para identificar movimento
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        
        # Quantificar o movimento
        movement_score = np.sum(thresh) / 255
        
        # Mostra o resultado
        cv2.imshow("Diferença entre quadros", thresh)
        print(f"Quantidade de movimento: {movement_score}") # faz esse escore somar no front
        
        # Atualiza o quadro anterior
        gray1 = gray2
        media = score/count
        
        if(movement_score >= media):
            score += movement_score
            movimentos_validos =+ 1
            

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if count > 200:
            break

    print(f"A média da tremedeira {media}")
    print(f"Sua pontuação total foi de {score}")
    print(f"{movimentos_validos} movimentos seus contaram!")
    cap.release()
    cv2.destroyAllWindows()

    return media


