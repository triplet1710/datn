from ultralytics import YOLO

# Load mô hình đã huấn luyện
model = YOLO('nghingo.pt')

# Đánh giá mô hình và lấy kết quả đánh giá
results = model.val(data='mydataset.yaml')

# Truy xuất và in các chỉ số đánh giá
# print("Class indices with average precision:", results.ap_class_index)
# print("Average precision for all classes:", results.box.all_ap)
# print("Mean average precision at IoU=0.50:", results.box.map50)
# print("Mean recall:", results.box.mr)
class_names = model.names
print("Các lớp trong mô hình YOLOv8:", class_names)