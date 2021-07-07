import random

def move(key):
  '''
    Retorna un estado para poder mover el bloque con fluides
    Parameters
    ----------
    key : Integer
      Código de la tecla entrada
    Returns
    ----------
    code : String
      Código que puede ser 'left', 'right', 'down', 'turn', devolver 
      caracteres vacios en caso de no ser ningun excenario
  '''
  code=""
  if key==82:
    code='turn'
  elif key==81:
    code='down'
  elif key==79:
      code= 'right'
  elif key==80:
    code='left'

  return code  
 
def set_pause(key):
  '''
    Retorna un booleando true, si la tecla de pausa se preciona.
    Parameters
    ----------
    key : Integer
      Código de la tecla entrada
    Returns
    ----------
    code : Boolean
      True si la tecla de pausa es presionada
  '''
  if key==19:
    return True

  return False

def score_message(score):
  '''
    Retorna el texto y color del mensaje de acuerdo al puntaje del jugador.
    Parameters

    - Para puntuación mayor o igual a 10 y menor a 15: "Meh" con un color Rojo: 231, verde: 76, azul: 60
    - Para puntuación mayor o igual a 15 y menor a 25: "Algo es algo" con un color Rojo: 245, verde: 176, azul: 65
    - Para puntuación mayor o igual a 25 y menor a 50: "Algo mejor" con un color Rojo: 235, verde: 152, azul: 78
    - Para puntuación mayor o igual a 50 y menor a 75: "No tan mal" con un color Rojo: 93, verde: 173, azul: 226
    - Para puntuación mayor o igual a 75 y menor a 100: "Mucho mejor" con un color Rojo: 46, verde: 204, azul: 113
    - Para puntuación mayor o igual a 100: "WOW" con un color al azar entre 0 y 255  para cada tono de color
    ----------
    score : Integer
      Puntaje de la partida
    Returns
    ----------
    message : String
      Texto para el jugador
    color: Truple
      Códificación RGB para mostrar colores en pantalla
  '''
  message='None'
  color = (0,0,0)

  if score >= 10 and score < 15:
    message = "Meh"
    color = (231,76,60)
    return message, color
  elif score >= 15 and score < 25:
    message = "Algo es algo"
    color = (245,176,65)
    return message, color
  elif score >= 25 and score < 50:
    message = "Algo mejor"
    color = (235,152,78)
    return message, color
  elif score >= 50 and score < 75:
    message = "No tan mal"
    color = (93,173,226)
    return message, color
  elif score >= 75 and score < 100:
    message = "Mucho mejor"
    color = (46,204,113)
    return message, color
  elif score > 100:
    message = "WOW"
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    color = (color1,color2,color3)
    return message, color
  else:
    return None, (0,0,0)