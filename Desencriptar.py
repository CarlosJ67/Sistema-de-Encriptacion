from FrmDesencriptar import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class Desencriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Funciones para desencriptar texto
        self.btnCargar.clicked.connect(self.cargar_archivo_texto)
        self.btnDesencriptar.clicked.connect(self.desencriptar_datos_texto)
        self.btnLimpiar.clicked.connect(self.limpiar_texto)

        # Funciones para desencriptar imagen
        self.btnCargar_2.clicked.connect(self.cargar_archivo_imagen)
        self.btnDesencriptar_2.clicked.connect(self.desencriptar_datos_imagen)
        self.btnLimpiar_2.clicked.connect(self.limpiar_imagen)

        # Atributos para manejar archivos
        self.imagen_encriptada = None

    # --- Funciones para texto ---
    def cargar_archivo_texto(self):
        # Abrir cuadro de diálogo para cargar archivo de texto
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Mensaje Encriptado",
            "",
            "Archivos de Texto (*.txt);;Todos los Archivos (*)",
            options=opciones,
        )

        if archivo:
            try:
                with open(archivo, "r") as file:
                    mensaje_encriptado = file.read()
                self.lblMensajeEncriptado_2.setText(mensaje_encriptado)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo: {e}")

    def desencriptar_datos_texto(self):
        mensaje_encriptado = self.lblMensajeEncriptado_2.text()

        if not mensaje_encriptado:
            QMessageBox.warning(self, "Error", "No hay mensaje encriptado cargado.")
            return

        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"

        try:
            mensaje_encriptado_bytes = bytes(eval(mensaje_encriptado))

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(mensaje_encriptado_bytes) + decryptor.finalize()

            unpadder = padding.PKCS7(128).unpadder()
            unpadded_data = unpadder.update(padded_data) + unpadder.finalize()

            mensaje_desencriptado = unpadded_data.decode('utf-8')
            self.lblMensajeDesencriptado.setText(mensaje_desencriptado)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo desencriptar el mensaje: {e}")

    def limpiar_texto(self):
        self.lblMensajeEncriptado_2.clear()
        self.lblMensajeDesencriptado.clear()

    # --- Funciones para imágenes ---
    def cargar_archivo_imagen(self):
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Imagen Encriptada",
            "",
            "Archivos Encriptados (*.enc);;Todos los Archivos (*)"
        )
        if archivo:
            try:
                with open(archivo, 'rb') as f:
                    self.imagen_encriptada = f.read()
                QMessageBox.information(self, "Carga Exitosa", "Imagen encriptada cargada correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo: {e}")

    def desencriptar_datos_imagen(self):
        if not self.imagen_encriptada:
            QMessageBox.warning(self, "Error", "Por favor, carga una imagen encriptada primero.")
            return

        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"

        try:
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(self.imagen_encriptada) + decryptor.finalize()

            unpadder = padding.PKCS7(128).unpadder()
            imagen_datos = unpadder.update(padded_data) + unpadder.finalize()

            pixmap = QPixmap()
            pixmap.loadFromData(imagen_datos)

            if pixmap.isNull():
                QMessageBox.warning(self, "Error", "No se pudo cargar la imagen desencriptada.")
            else:
                self.label_2.setPixmap(pixmap)
                self.label_2.setScaledContents(True)
                QMessageBox.information(self, "Desencriptación Exitosa", "La imagen ha sido desencriptada y mostrada.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo desencriptar la imagen: {e}")

    def limpiar_imagen(self):
        self.label_2.clear()
        self.imagen_encriptada = None
        QMessageBox.information(self, "Limpieza Exitosa", "Los datos de la imagen han sido limpiados.")
