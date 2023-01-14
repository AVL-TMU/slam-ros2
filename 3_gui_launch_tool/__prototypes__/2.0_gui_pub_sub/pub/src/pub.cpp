#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include <QtWidgets>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class MinimalPublisher: public rclcpp::Node{
    public:
        rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
        size_t count_;
        MinimalPublisher()
        : Node("gui_tool_node"), count_(0)
        {
            publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
        }
        void callback_function(){
            auto message = std_msgs::msg::String();
            message.data = "Hello, world!" + std::to_string(count_++);
            RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
            publisher_->publish(message);
        }
        
};


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QWidget *window = new QWidget;
    window->setFixedSize(500, 500);

    rclcpp::init(argc, argv);    

    // this method interestingly did not work in the button callback
    // MinimalPublisher MinimalPublisher_;
    // MinimalPublisher_.MinimalPublisher::callback_function();

    MinimalPublisher *miniPub = new MinimalPublisher();
    

    QPushButton *button1 = new QPushButton("Send Pub");    
    QObject::connect(button1, &QPushButton::clicked, [=]() {
        miniPub->callback_function();
    });

    QVBoxLayout *mainLayout = new QVBoxLayout;
    mainLayout->addWidget(button1);
    mainLayout->setAlignment(Qt::AlignCenter);

    window->setLayout(mainLayout);
    window->show();

    return a.exec();
}