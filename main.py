import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
import os
import datetime
import cv2
from ultralytics import YOLO
import numpy as np
import mysql.connector 
import linear
from pyzbar.pyzbar import decode
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.w = linear.Linear_Regression()
    ##### cai dat thoi gian #######
        now = QDate.currentDate()
        current_date = now.toString('dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.uic.Date_label.setText(current_date)
        self.uic.Time_label.setText(current_time)
    ## khai bao nut
        self.uic.Button_start.clicked.connect(self.start)
        self.uic.Button_check.clicked.connect(self.check)
        self.uic.Button_save.clicked.connect(self.save)
        self.uic.button_exit.clicked.connect(self.exit)
        self.uic.Button_stop.clicked.connect(self.cancel)
    #### ket noi voi database ############
        self.conn = mysql.connector.connect(
                    host="127.0.0.1",       # Địa chỉ của MySQL server
                    user="root",   # Tên đăng nhập MySQL
                    password="tin171002",# Mật khẩu MySQL
                    database="datn"
            )
        self.cu = self.conn.cursor()
    def start(self):
        
        self.Work = Work(self.w)
        self.Work.start()
        self.Work.infor.connect(self.work_slot)
        # self.conn = mysql.connector.connect(
        #             host="127.0.0.1",       # Địa chỉ của MySQL server
        #             user="root",   # Tên đăng nhập MySQL
        #             password="tin171002",# Mật khẩu MySQL
        #             database="datn"
        #     )
        # self.cu = self.conn.cursor()
    def check(self):
        select = """
                SELECT e.name_employee,  s.weight, s.num_shrimp
                FROM employees e
                JOIN shrimp_batches s ON e.id_employees = s.id_employees
                WHERE e.id_employees= %s;
            """
        self.cu.execute(select, (self.uic.comboBox.currentText(),))
        print(self.uic.comboBox.currentText())
        results = self.cu.fetchall()
        
        self.uic.name_lable.setText(results[0][0])
        s_w =0
        s_s = 0
        s_b =0
        for row in results:
            s_w = s_w+row[1]
            s_s = s_s + row[2]
            s_b = s_b +1 
        
        self.uic.total_weight_lable.setText(str(s_w))
        self.uic.total_shrimp_lable.setText(str(s_s))
        self.uic.total_batch_lable.setText(str(s_b))
    def save(self):
        insert_query = """
                        INSERT INTO shrimp_batches (id_employees,  weight, num_shrimp,timestamp )
                        VALUES (%s,  %s, %s,%s);
                        """
        
        # v = (int(self.uic.qr_lable.text()),10,10)
        # self.cu.execute(insert_query,v)
        self.cu.execute(insert_query,(self.uic.qr_lable.text(),self.uic.lable_weight.text(),self.uic.lable_nums.text(),datetime.datetime.now()))
        self.conn.commit()

    def work_slot(self,pic,num_shrimp,total_area,total_weight,qr_value):
        self.area = total_area
        self.uic.label_img.setPixmap(QPixmap.fromImage(pic))
        # self.uic.lable_contourarea.setText(str(total_area))
        self.uic.lable_weight.setText(str(total_weight))

        self.uic.lable_nums.setText(str(num_shrimp))
        self.value_qr = qr_value
        if qr_value != "0":
            self.uic.qr_lable.setText(qr_value)

    def exit(self):
        
        reply = QMessageBox.question(self, 'Exit Window', 'Are you sure you want to exit the window',
                                     QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        elif reply == QMessageBox.No:
            pass
        else:
            pass
        
    def cancel(self):
        self.uic.lable_weight_2.setText(str(self.area))
        
class Work(QThread):
    def __init__(self,w):
        super().__init__()
        self.w_0 = w[0][0]
        self.w_1 = w[1][0]
        self.fps =0
    infor = pyqtSignal(QImage,int,int,float,str)
    def run(self):
        self.status_for_running = True
        model = YOLO("yolov8s.pt")
        cap = cv2.VideoCapture(0)
        # frame_count = 0
        # start_time = time.time()
        while self.status_for_running:
            ret, frame = cap.read()
            if not ret:
                return
            # frame_count += 1

    # Tính thời gian trôi qua
    #         elapsed_time = time.time() - start_time
    # # Tính FPS sau mỗi 1 giây
    #         if elapsed_time > 1:
    #             self.fps = frame_count / elapsed_time
    #     # Đặt lại bộ đếm
    #             frame_count = 0
    #             start_time = time.time()
    #         cv2.putText(frame, f"FPS: {self.fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            ###### QR code ##############
            decoded_objects = decode(frame)
            qr_value = '0'
            for obj in decoded_objects:
                qr_value = obj.data.decode("utf-8")
                (x, y, w, h) = obj.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, obj.data.decode("utf-8"), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            results = model(frame)
            total_area = 0
            total_weight = 0
            cnt_shrimp = 0
            if results[0].masks is not None:
                masks = (results[0].masks.data.numpy()*1).astype('uint8')
                for i,mask in enumerate(masks):
                    x1,y1,x2,y2,c,id = results[0].boxes.data[i].numpy()
                    if c > 0.6:
                ############ mask ############
                        original_height, original_width = frame.shape[:2]

                        mask_resized = cv2.resize(mask, (original_width, original_height), interpolation=cv2.INTER_NEAREST)
                        mask = mask_resized
                        colored_mask = np.zeros_like(frame, dtype=np.uint8)

                ########## weight ################
                        area = np.sum(mask)
                        weight = self.w_0 + self.w_1*area
                        weight = round(weight, 2)
                        if weight < 22:
                            cv2.putText(frame, "TOM KHONG DAT CHAT LUONG", (int(x1),int(y1)), 1, 1, (0, 0, 255))
                            
                            colored_mask[mask_resized > 0] = (0, 0, 255)
                            frame = cv2.addWeighted(frame, 1, colored_mask, 0.5, 0)

                        else:
                            cv2.putText(frame, f"{c:.1f}", (int(x1),int(y1)), 1, 1, (0, 0, 255))
                            
                            colored_mask[mask_resized > 0] = (0, 255, 0)
                            frame = cv2.addWeighted(frame, 1, colored_mask, 0.5, 0)
                        total_weight = total_weight + weight
                        total_area = total_area + area
                ########## center ###############

                        M = cv2.moments(mask)
                        if M["m00"] != 0:
                            center_x = int(M["m10"] / M["m00"])
                            center_y = int(M["m01"] / M["m00"])
                    
                        cv2.circle(frame, (int(center_x), int(center_y)), 4, (255, 0, 0), -1)
                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                        # cv2.putText(frame, str(area) , (int(x1),int(y1)), 1, 1, (0, 0, 255))
                        # cv2.putText(frame, f"{c:.1f}", (int(x1),int(y1)), 1, 1, (0, 0, 255))
                        cnt_shrimp = cnt_shrimp + 1

            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertir_QT = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
            pic = convertir_QT.scaled(640, 460, Qt.KeepAspectRatio)
            self.infor.emit(pic,cnt_shrimp,total_area,total_weight,qr_value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
    