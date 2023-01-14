#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include <QtWidgets>

// #include "rclcpp/rclcpp.hpp"
// #include "std_msgs/msg/string.hpp"

// using namespace std::chrono_literals;

// class MinimalPublisher: public rclpp::Node{
//     public:
//         MinimalPublisher()
//         : Node("launch_tool_node"), count_(0)
//         {
//             publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
//         }
//     private:
//         void callback_function(){
//             auto message = std_msgs::msg::String();
//             message.data = "Hello, world!" + std::to_string(count_++);
//             RCLPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
//             publisher_->publish(message);
//         }
//         rclpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
//         size_t count_;
// };



int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QWidget *window = new QWidget;
    window->setFixedSize(500, 500);

    QLabel *label1 = new QLabel("Label 1:");
    QLabel *label2 = new QLabel("Label 2:");
    QLabel *label3 = new QLabel("Label 3:");
    QLabel *label4 = new QLabel("Label 4:");

    QLineEdit *textField1 = new QLineEdit;
    QLineEdit *textField2 = new QLineEdit;
    QLineEdit *textField3 = new QLineEdit;
    QLineEdit *textField4 = new QLineEdit;

    QHBoxLayout *labelTextFieldLayout = new QHBoxLayout;
    labelTextFieldLayout->addWidget(label1);
    labelTextFieldLayout->addWidget(textField1);
    labelTextFieldLayout->addWidget(label2);
    labelTextFieldLayout->addWidget(textField2);
    labelTextFieldLayout->addWidget(label3);
    labelTextFieldLayout->addWidget(textField3);
    labelTextFieldLayout->addWidget(label4);
    labelTextFieldLayout->addWidget(textField4);
    labelTextFieldLayout->setAlignment(Qt::AlignCenter);
    labelTextFieldLayout->setSpacing(20);

    QPushButton *button1 = new QPushButton("Button 1");
    QPushButton *button2 = new QPushButton("Button 2");

    QHBoxLayout *buttonLayout = new QHBoxLayout;
    buttonLayout->addWidget(button1);
    buttonLayout->addWidget(button2);
    buttonLayout->setAlignment(Qt::AlignCenter);
    buttonLayout->setSpacing(20);

    QVBoxLayout *mainLayout = new QVBoxLayout;
    mainLayout->addLayout(labelTextFieldLayout);
    mainLayout->addLayout(buttonLayout);

    window->setLayout(mainLayout);
    window->show();

    return a.exec();
}