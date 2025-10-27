/**
 * 重构设计示例：面向对象的CANModule
 * 
 * 这个文件展示了如何将现有的C代码重构为更好的面向对象设计
 * 注意：这是设计建议，不是实际的代码替换
 */

#ifndef REFACTORED_CAN_MODULE_H
#define REFACTORED_CAN_MODULE_H

#include <stdbool.h>
#include <stddef.h>

// 前向声明，避免直接依赖系统头文件
struct can_frame;
struct sockaddr_can;
struct ifreq;

// =============================================================================
// 方案1: C++风格的CANModule类设计
// =============================================================================

#ifdef __cplusplus

class CANModule {
private:
    // 将TCan作为内部状态，而不是外部传递的参数
    struct {
        char* iface;
        void* addr;          // 原 struct sockaddr_can addr
        void* ifr;           // 原 struct ifreq ifr
        unsigned int id;
        int socket;
        bool is_connected;
    } can_device;
    
    // 私有辅助方法
    bool validateConnection() const;
    void logError(const char* operation, int error_code) const;

public:
    // 构造函数和析构函数
    explicit CANModule(const char* interface_name);
    ~CANModule();
    
    // 禁止拷贝构造和赋值（RAII原则）
    CANModule(const CANModule&) = delete;
    CANModule& operator=(const CANModule&) = delete;
    
    // 连接管理
    bool open(unsigned int node_id);
    bool close();
    bool isConnected() const { return can_device.is_connected; }
    
    // 状态控制
    bool setOperational();
    bool setPreOperational();
    
    // 消息传输（封装了PDO2细节）
    bool sendMessage(const unsigned char* data, size_t size);
    bool receiveMessage(struct can_frame& frame);
    bool sendAndReceive(const unsigned char* data, size_t size, struct can_frame& response);
    
    // 数据转换工具（静态方法，可以独立使用）
    static void setDataInt(unsigned char* data, int value);
    static void setDataFloat(unsigned char* data, float value);
    static int intFromData(const unsigned char* data);
    static float floatFromData(const unsigned char* data);
    
    // 获取设备信息
    const char* getInterfaceName() const { return can_device.iface; }
    unsigned int getNodeId() const { return can_device.id; }
};

#endif // __cplusplus

// =============================================================================
// 方案2: C语言的"伪面向对象"设计
// =============================================================================

// 前向声明
typedef struct CANModule_t CANModule_t;

// 构造和析构
CANModule_t* CANModule_create(const char* interface_name);
void CANModule_destroy(CANModule_t* module);

// 连接管理
int CANModule_open(CANModule_t* module, unsigned int node_id);
int CANModule_close(CANModule_t* module);
int CANModule_isConnected(const CANModule_t* module);

// 状态控制
int CANModule_setOperational(CANModule_t* module);
int CANModule_setPreOperational(CANModule_t* module);

// 消息传输
int CANModule_sendMessage(CANModule_t* module, const unsigned char* data, size_t size);
int CANModule_receiveMessage(CANModule_t* module, struct can_frame* frame);
int CANModule_sendAndReceive(CANModule_t* module, const unsigned char* data, size_t size, struct can_frame* response);

// 数据转换（独立函数）
void CANModule_setDataInt(unsigned char* data, int value);
void CANModule_setDataFloat(unsigned char* data, float value);
int CANModule_intFromData(const unsigned char* data);
float CANModule_floatFromData(const unsigned char* data);

// 信息获取
const char* CANModule_getInterfaceName(const CANModule_t* module);
unsigned int CANModule_getNodeId(const CANModule_t* module);

// =============================================================================
// 设计优势分析
// =============================================================================

/*
重构后的优势：

1. 封装性 (Encapsulation)
   - TCan状态被封装在CANModule内部
   - 外部代码不需要直接操作TCan结构体
   - 减少了状态管理的复杂性

2. 职责单一 (Single Responsibility)
   - CANModule专门负责CAN通信
   - 清晰的接口边界
   - 更容易测试和维护

3. 资源管理 (RAII)
   - 构造函数中初始化资源
   - 析构函数中清理资源
   - 避免内存泄漏和资源泄漏

4. 错误处理
   - 统一的错误处理机制
   - 更好的错误信息和日志
   - 状态验证

5. 扩展性
   - 容易添加新功能
   - 可以支持多个CAN设备
   - 更好的配置管理

使用示例：

// C++版本
CANModule can_module("can0");
if (can_module.open(127)) {
    can_module.setOperational();
    unsigned char data[] = "MO=1";
    can_module.sendMessage(data, 4);
}

// C版本
CANModule_t* module = CANModule_create("can0");
if (CANModule_open(module, 127) == 0) {
    CANModule_setOperational(module);
    unsigned char data[] = "MO=1";
    CANModule_sendMessage(module, data, 4);
}
CANModule_destroy(module);
*/

#endif // REFACTORED_CAN_MODULE_H