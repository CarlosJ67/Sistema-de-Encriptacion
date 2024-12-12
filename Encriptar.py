from FrmEncriptar import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Encriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Conexiones para encriptar texto
        self.btnEncriptar.clicked.connect(self.encrypt_data_AES)
        self.btnLimpiar.clicked.connect(self.limpiar_texto)
        self.btnDescargar.clicked.connect(self.descargar_mensaje)

        # Conexiones para encriptar imágenes
        self.btnCargar_2.clicked.connect(self.cargar_imagen)
        self.btnEncriptar_2.clicked.connect(self.encriptar_imagen)
        self.btnDescargar_2.clicked.connect(self.descargar_imagen_encriptada)
        self.btnLimpiar_2.clicked.connect(self.limpiar_imagen)

        # Atributos para manejar imágenes
        self.imagen_path = None
        self.imagen_encriptada = None

    # --- Funciones para texto ---
    def encrypt_data_AES(self):
        data = self.txtMensaje.toPlainText()
        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode('utf-8'))
        padded_data += padder.finalize()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        self.lblMensajeEncriptado.setText(f'{ciphertext}')

    def limpiar_texto(self):
        self.lblMensajeEncriptado.clear()
        self.txtMensaje.clear()

    def descargar_mensaje(self):
        mensaje_encriptado = self.lblMensajeEncriptado.text()
        if not mensaje_encriptado:
            QMessageBox.warning(self, "Error", "No hay mensaje encriptado para descargar.")
            return
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar Mensaje Encriptado", "", "Archivos de Texto (*.txt);;Todos los Archivos (*)", options=opciones
        )
        if archivo:
            try:
                with open(archivo, "w") as file:
                    file.write(mensaje_encriptado)
                QMessageBox.information(self, "Éxito", "El mensaje se ha guardado correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {e}")

    # --- Funciones para imágenes ---
    def cargar_imagen(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los archivos (*)",
            options=opciones,
        )
        if archivo:
            self.imagen_path = archivo
            self.lblimagen_2.setText(f"Imagen cargada: {archivo}")
            QMessageBox.information(self, "Carga exitosa", "Imagen cargada correctamente.")

    def encriptar_imagen(self):
        if not self.imagen_path:
            QMessageBox.warning(self, "Error", "Por favor, carga una imagen primero.")
            return
        try:
            with open(self.imagen_path, "rb") as file:
                imagen_bytes = file.read()

            key = b"123456789101112131415161718_UTXJ"  # Clave de 32 bytes
            iv = b"TI_UTXJ2024ENCRI"  # Vector de inicialización de 16 bytes
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(imagen_bytes) + padder.finalize()

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            self.imagen_encriptada = encryptor.update(padded_data) + encryptor.finalize()

            QMessageBox.information(self, "Encriptación exitosa", "La imagen ha sido encriptada correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al encriptar la imagen: {e}")

    def descargar_imagen_encriptada(self):
        if not self.imagen_encriptada:
            QMessageBox.warning(self, "Error", "No hay imagen encriptada para descargar.")
            return
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Imagen Encriptada",
            "",
            "Archivos Encriptados (*.enc);;Todos los Archivos (*)",
            options=opciones,
        )
        if archivo:
            try:
                with open(archivo, "wb") as file:
                    file.write(self.imagen_encriptada)
                QMessageBox.information(self, "Guardado exitoso", "La imagen encriptada se guardó correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {e}")

    def limpiar_imagen(self):
        self.lblimagen_2.clear()
        self.imagen_path = None
        self.imagen_encriptada = None
