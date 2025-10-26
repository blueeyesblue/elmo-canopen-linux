#!/usr/bin/env python3
"""
SVG类图生成器 - 用于生成Elmo CANopen项目的类图
可以根据需要修改颜色、布局和内容
"""


def create_svg_header():
    """创建SVG头部和样式定义"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1000" height="700" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .title { font-family: Arial, sans-serif; font-size: 18px; 
               font-weight: bold; text-anchor: middle; fill: #000; }
      .class-name { font-family: Arial, sans-serif; font-size: 14px; 
                    font-weight: bold; text-anchor: middle; fill: #000; }
      .attribute { font-family: Arial, sans-serif; font-size: 11px; 
                   text-anchor: start; fill: #000; }
      .method { font-family: Arial, sans-serif; font-size: 11px; 
                text-anchor: start; fill: #000; }
      .enum { font-family: Arial, sans-serif; font-size: 11px; 
              text-anchor: start; font-style: italic; fill: #000; }
      .arrow { stroke: #333; stroke-width: 2; fill: none; 
               marker-end: url(#arrowhead); }
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" 
            refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333" />
    </marker>
  </defs>
  
  <!-- Background -->
  <rect x="0" y="0" width="1000" height="700" fill="white" 
        stroke="#ddd" stroke-width="1"/>
  
  <!-- Title -->
  <text x="500" y="30" class="title">Elmo CANopen 项目类图</text>'''


def create_tcan_structure():
    """创建TCan结构体图"""
    return '''
  <!-- TCan Structure -->
  <rect x="50" y="60" width="250" height="180" fill="#e6f3ff" 
        stroke="#0066cc" stroke-width="2" rx="5"/>
  <text x="175" y="80" class="class-name">TCan (结构体)</text>
  <line x1="60" y1="85" x2="290" y2="85" stroke="#0066cc" 
        stroke-width="1"/>
  <text x="70" y="105" class="attribute">- char *iface</text>
  <text x="70" y="120" class="attribute">- struct sockaddr_can addr</text>
  <text x="70" y="135" class="attribute">- struct ifreq ifr</text>
  <text x="70" y="150" class="attribute">- unsigned int id</text>
  <text x="70" y="165" class="attribute">- int socket</text>
  <line x1="60" y1="175" x2="290" y2="175" stroke="#0066cc" 
        stroke-width="1"/>
  <text x="70" y="195" class="method">构造/析构函数</text>
  <text x="70" y="210" class="method">通信管理函数</text>
  <text x="70" y="225" class="method">状态控制函数</text>'''


def create_mode_enum():
    """创建Mode枚举图"""
    return '''
  <!-- Mode Enum -->
  <rect x="350" y="60" width="180" height="100" fill="#fff2e6" 
        stroke="#ff6600" stroke-width="2" rx="5"/>
  <text x="440" y="80" class="class-name">Mode (枚举)</text>
  <line x1="360" y1="85" x2="520" y2="85" stroke="#ff6600" 
        stroke-width="1"/>
  <text x="370" y="105" class="enum">MODE_POS = 5</text>
  <text x="370" y="120" class="enum">MODE_TORQUE = 1</text>
  <line x1="360" y1="130" x2="520" y2="130" stroke="#ff6600" 
        stroke-width="1"/>
  <text x="370" y="150" class="method">位置控制模式</text>'''


def create_can_module():
    """创建CAN模块图"""
    can_methods = [
        "+ TCan* TCanConstruct(const char *iface)",
        "+ void TCanDestruct(TCan *can)",
        "+ int TCanOpen(TCan *can, int canid)",
        "+ int TCanClose(TCan *can)",
        "+ int setOperational(TCan *can)",
        "+ int sendPDO2(TCan *can, int size, char *data)",
        "+ int receivePDO2(TCan *can, can_frame *frame)",
        "+ void setDataInt/Float(char *data, value)",
        "+ int/float intFromData/floatFromData(char *data)",
        "+ void createFrame(can_frame *frame, ...)"
    ]
    
    result = '''
  <!-- CAN Module -->
  <rect x="50" y="280" width="280" height="200" fill="#f0fff0" 
        stroke="#009900" stroke-width="2" rx="5"/>
  <text x="190" y="300" class="class-name">CAN 通信模块 (can.h/can.c)</text>
  <line x1="60" y1="305" x2="320" y2="305" stroke="#009900" 
        stroke-width="1"/>'''
    
    y_pos = 325
    for method in can_methods:
        result += f'\n  <text x="70" y="{y_pos}" class="method">'
        result += f'{method}</text>'
        y_pos += 15
    
    return result


def create_elmo_module():
    """创建Elmo模块图"""
    elmo_methods = [
        "+ int sendEchoMessage(TCan *can)",
        "+ int setPosition(TCan *can, int pos)",
        "+ int getPosition(TCan *can, int *pos)",
        "+ int setForce(TCan *can, float force)",
        "+ int getForce(TCan *can, float *force)",
        "+ int startMotor(TCan *can)",
        "+ int stopMotor(TCan *can)",
        "+ int beginMotion(TCan *can)",
        "+ int setUnitMode(TCan *can, Mode mode)",
        "+ int setSpeed(TCan *can, int speed)",
        "+ int setAbsolutePosition(TCan *can, int pos)",
        "+ int setTorque(TCan *can, float torque)",
        "+ int setLimits(TCan *can, int vmin, vmax, ...)"
    ]
    
    result = '''
  <!-- Elmo Module -->
  <rect x="380" y="280" width="300" height="240" fill="#ffe6e6" 
        stroke="#cc0000" stroke-width="2" rx="5"/>
  <text x="530" y="300" class="class-name">Elmo 控制模块 (elmo.h/elmo.c)</text>
  <line x1="390" y1="305" x2="670" y2="305" stroke="#cc0000" 
        stroke-width="1"/>'''
    
    y_pos = 325
    for method in elmo_methods:
        result += f'\n  <text x="400" y="{y_pos}" class="method">'
        result += f'{method}</text>'
        y_pos += 15
    
    return result


def create_main_and_relationships():
    """创建主程序模块和关系图"""
    return '''
  <!-- Main Application -->
  <rect x="720" y="280" width="220" height="120" fill="#f5f5f5" 
        stroke="#333" stroke-width="2" rx="5"/>
  <text x="830" y="300" class="class-name">主程序 (main.c)</text>
  <line x1="730" y1="305" x2="930" y2="305" stroke="#333" 
        stroke-width="1"/>
  <text x="740" y="325" class="method">+ int main()</text>
  <text x="740" y="340" class="method">+ void test(TCan *can)</text>
  <text x="740" y="355" class="method">+ void test_position(TCan *can)</text>
  <text x="740" y="370" class="method">+ void test_force(TCan *can)</text>
  <text x="740" y="385" class="method">+ void print_info(TCan *can)</text>
  
  <!-- Relationships -->
  <line x1="175" y1="240" x2="175" y2="270" class="arrow"/>
  <line x1="330" y1="380" x2="370" y2="380" class="arrow"/>
  <line x1="680" y1="340" x2="710" y2="340" class="arrow"/>
  <line x1="440" y1="160" x2="440" y2="270" class="arrow"/>'''


def create_config_and_protocol():
    """创建配置和协议信息"""
    return '''
  <!-- Constants and Configuration -->
  <rect x="50" y="540" width="300" height="100" fill="#f9f9f9" 
        stroke="#666" stroke-width="1" rx="3"/>
  <text x="200" y="560" class="class-name">配置常量</text>
  <line x1="60" y1="565" x2="340" y2="565" stroke="#666" 
        stroke-width="1"/>
  <text x="70" y="585" class="attribute">#define CAN_INTERFACE "can0"</text>
  <text x="70" y="600" class="attribute">#define CANOPEN_ID 127</text>
  <text x="70" y="615" class="attribute">PDO2 COB-ID: 0x301-0x37f (发送)</text>
  <text x="70" y="630" class="attribute">RPDO2 COB-ID: 0x281-0x2ff (接收)</text>
  
  <!-- Protocol Details -->
  <rect x="400" y="540" width="300" height="100" fill="#f0f8ff" 
        stroke="#4169e1" stroke-width="1" rx="3"/>
  <text x="550" y="560" class="class-name">CANopen 协议细节</text>
  <line x1="410" y1="565" x2="690" y2="565" stroke="#4169e1" 
        stroke-width="1"/>
  <text x="420" y="585" class="attribute">• 使用 PDO (Process Data Object)</text>
  <text x="420" y="600" class="attribute">• 支持位置和扭矩控制模式</text>
  <text x="420" y="615" class="attribute">• 命令格式: ASCII + 参数</text>
  <text x="420" y="630" class="attribute">• 数据长度: 4-8 字节</text>
  
</svg>'''


def generate_svg_class_diagram():
    """生成完整的SVG类图"""
    svg_parts = [
        create_svg_header(),
        create_tcan_structure(),
        create_mode_enum(),
        create_can_module(),
        create_elmo_module(),
        create_main_and_relationships(),
        create_config_and_protocol()
    ]
    
    return ''.join(svg_parts)


def main():
    """主函数 - 生成SVG文件"""
    svg_content = generate_svg_class_diagram()
    
    # 写入文件
    with open('class_diagram.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print("SVG类图已生成: class_diagram.svg")
    print("\n可以修改的配置项:")
    print("- 在各个create_*函数中修改颜色")
    print("- 在create_svg_header中修改尺寸和字体")
    print("- 在各个模块函数中修改布局和内容")


if __name__ == "__main__":
    main()