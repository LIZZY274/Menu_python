import cv2
import numpy as np
import math


def traslacion():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    num_rows, num_cols = img.shape[:2]
    translation_matrix = np.float32([[1, 0, 70], [0, 1, 110]])
    img_translation = cv2.warpAffine(img, translation_matrix, (num_cols + 70, num_rows + 110))

    cv2.imshow('Traslación', img_translation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def warping():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    matrix = cv2.getAffineTransform(pts1, pts2)
    img_warp = cv2.warpAffine(img, matrix, (cols, rows))

    cv2.imshow('Warping', img_warp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cambio_formato():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    cv2.imwrite('images/output.jpg', img)
    print("Imagen guardada como 'output.jpg'.")

def cambio_color():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    img_red = img.copy()

   
    img_red[:, :, 1] = 0  
    img_red[:, :, 2] = 0  

    cv2.imshow('Imagen en tonos rojos', img_red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def dividir_imagen():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    mitad = img.shape[1] // 2
    img_izquierda = img[:, :mitad]
    img_derecha = img[:, mitad:]

    cv2.imshow('Izquierda', img_izquierda)
    cv2.imshow('Derecha', img_derecha)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def escalar_imagen():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    img_resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('Imagen Escalada', img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def leer_imagen():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    cv2.imshow('Imagen leída', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def guardar_imagen():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    cv2.imwrite('images/guardada.png', img)
    print("Imagen guardada como 'guardada.png'.")

def proyeccion():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    rows, cols = img.shape[:2]
    projection_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0], [0, 0, 1]])
    img_proj = cv2.warpPerspective(img, projection_matrix, (cols, rows))

    cv2.imshow('Proyección', img_proj)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotacion():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    rows, cols = img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    img_rotated = cv2.warpAffine(img, rotation_matrix, (cols, rows))

    cv2.imshow('Rotación', img_rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transformacion():
    img = cv2.imread('images/input.png')
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    matrix = cv2.getAffineTransform(pts1, pts2)
    img_trans = cv2.warpAffine(img, matrix, (cols, rows))

    cv2.imshow('Transformación', img_trans)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Traslación de imagen")
        print("2. Warping de imagen")
        print("3. Cambio de formato")
        print("4. Cambio de color")
        print("5. Dividir imagen")
        print("6. Escalar imagen")
        print("7. Leer imagen")
        print("8. Guardar imagen")
        print("9. Proyección de imagen")
        print("10. Rotación de imagen")
        print("11. Transformación")
        print("12. Salir")
        
        opcion = input("Selecciona una opción (1-12): ")

        if opcion == '1':
            traslacion()
        elif opcion == '2':
            warping()
        elif opcion == '3':
            cambio_formato()
        elif opcion == '4':
            cambio_color()
        elif opcion == '5':
            dividir_imagen()
        elif opcion == '6':
            escalar_imagen()
        elif opcion == '7':
            leer_imagen()
        elif opcion == '8':
            guardar_imagen()
        elif opcion == '9':
            proyeccion()
        elif opcion == '10':
            rotacion()
        elif opcion == '11':
            transformacion()
        elif opcion == '12':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
