import torch
import torch.nn as nn
import time
import sys

def test_gpu_acceleration():
    """
    测试GPU加速对常见计算任务的性能提升。
    这些任务可能在OpenCode辅助的AI编程或数据处理项目中出现。
    """
    print("=== GPU加速性能测试 ===\n")
    
    # 检查CUDA是否可用
    cuda_available = torch.cuda.is_available()
    device = torch.device("cuda" if cuda_available else "cpu")
    print(f"1. GPU (CUDA) 可用状态: {cuda_available}")
    if cuda_available:
        print(f"   当前设备: {torch.cuda.get_device_name(0)}")
        print(f"   CUDA版本: {torch.version.cuda}")
    
    # 测试1: 大规模矩阵运算 (常见于机器学习项目)
    print("\n2. 测试大规模矩阵运算 (尺寸: 5000x5000):")
    size = 5000
    matrix_a = torch.randn(size, size, device=device)
    matrix_b = torch.randn(size, size, device=device)
    
    start_time = time.time()
    result = torch.mm(matrix_a, matrix_b)
    torch.cuda.synchronize() if cuda_available else None
    elapsed_time = time.time() - start_time
    print(f"   矩阵乘法耗时: {elapsed_time:.3f} 秒")
    
    # 测试2: 神经网络前向传播 (模拟AI模型推理)
    print("\n3. 测试神经网络前向传播:")
    # 模拟一个中等复杂度的神经网络
    class SimpleNN(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(1000, 512)
            self.fc2 = nn.Linear(512, 256)
            self.fc3 = nn.Linear(256, 10)
            self.relu = nn.ReLU()
        
        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.fc3(x)
            return x
    
    model = SimpleNN().to(device)
    input_data = torch.randn(64, 1000, device=device)  # 批量大小64
    
    # Warm-up
    for _ in range(10):
        _ = model(input_data)
    
    # 正式测试
    start_time = time.time()
    for _ in range(100):
        output = model(input_data)
    torch.cuda.synchronize() if cuda_available else None
    elapsed_time = time.time() - start_time
    print(f"   100次前向传播平均耗时: {(elapsed_time/100*1000):.2f} 毫秒/次")
    
    # 测试3: 数据处理任务 (如大型张量操作)
    print("\n4. 测试数据处理任务:")
    large_tensor = torch.randn(10000, 1000, device=device)
    
    start_time = time.time()
    # 执行一系列数据转换操作
    normalized = (large_tensor - large_tensor.mean()) / large_tensor.std()
    processed = torch.sigmoid(normalized) * 100
    result_sum = processed.sum()
    torch.cuda.synchronize() if cuda_available else None
    elapsed_time = time.time() - start_time
    print(f"   大数据处理耗时: {elapsed_time:.3f} 秒")
    
    # 性能对比总结
    print("\n=== 性能影响总结 ===")
    if cuda_available:
        print("✅ GPU加速已启用，对以下OpenCode相关任务有帮助:")
        print("   • 本地模型推理/微调")
        print("   • 数据预处理和特征工程")
        print("   • 模型训练和验证")
        print("   • 大型数值计算")
        print("\n⚠️  GPU对以下任务无直接加速:")
        print("   • OpenCode插件本身的响应速度")
        print("   • 代码补全和建议生成")
        print("   • 与远程API的通信速度")
    else:
        print("❌ GPU加速未启用，所有计算均在CPU上执行。")
        print("   如需启用，请确保:")
        print("   1. WSL中已正确安装CUDA Toolkit")
        print("   2. PyTorch安装了CUDA版本")
        print("   3. 运行此脚本前激活了虚拟环境")

def check_opencode_usage_scenarios():
    """
    检查哪些OpenCode使用场景能从GPU加速中受益
    """
    print("\n\n=== OpenCode使用场景分析 ===")
    
    scenarios = {
        "高受益场景": [
            "在OpenCode项目中运行本地LLM推理",
            "执行数据科学/机器学习项目代码",
            "训练或微调小型AI模型",
            "处理大型数据集进行可视化",
            "运行需要矩阵运算的科学计算"
        ],
        "低受益场景": [
            "OpenCode的代码补全和语法检查",
            "与ChatGPT/Kimi等远程API交互",
            "日常的代码编辑和导航",
            "项目管理和小型脚本执行"
        ]
    }
    
    print("1. 高受益场景 (GPU加速效果显著):")
    for i, scenario in enumerate(scenarios["高受益场景"], 1):
        print(f"   {i}. {scenario}")
    
    print("\n2. 低受益场景 (GPU加速效果有限):")
    for i, scenario in enumerate(scenarios["低受益场景"], 1):
        print(f"   {i}. {scenario}")

if __name__ == "__main__":
    # 执行性能测试
    test_gpu_acceleration()
    
    # 分析OpenCode使用场景
    check_opencode_usage_scenarios()
    
    # 最终建议
    print("\n=== 最终建议 ===")
    print("1. 如果您的OpenCode项目涉及本地AI模型、数据科学或数值计算，GPU加速至关重要。")
    print("2. 如果主要使用OpenCode进行日常编码并调用远程API，GPU加速的收益有限。")
    print("3. 建议在需要GPU加速的项目中使用虚拟环境，并确保安装了CUDA版本的PyTorch/TensorFlow。")
