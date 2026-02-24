import os
import sys
import subprocess
import json
import shutil
import glob

def print_step(msg):
    """Utility function to print formatted step headers."""
    print(f"\n[{'='*50}]\n🚀 {msg}\n[{'='*50}]")

def check_dependencies():
    """Check if required command-line tools are installed."""
    print_step("Step 1: Checking base dependencies (Git, Node, npm)")
    deps = ["git", "node", "npm"]
    for dep in deps:
        try:
            # Hide output but check return code
            subprocess.run([dep, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            print(f"✅ Found {dep}")
        except FileNotFoundError:
            print(f"❌ Error: '{dep}' not found. Please ensure it is installed and added to your system PATH!")
            sys.exit(1)

def find_matlab():
    """Auto-locate the latest MATLAB installation path on Windows."""
    print_step("Step 2: Auto-locating MATLAB installation path")
    matlab_search_path = r"C:\Program Files\MATLAB\R20*"
    paths = glob.glob(matlab_search_path)
    
    if not paths:
        print("❌ Error: Could not find MATLAB in the default directory (C:\\Program Files\\MATLAB).")
        sys.exit(1)
    
    # Sort descending to get the newest version (e.g., R2026a > R2025b)
    paths.sort(reverse=True)
    matlab_root = paths[0]
    print(f"✅ Found latest MATLAB version: {matlab_root}")
    return matlab_root

def install_matlab_engine(matlab_root):
    """Install the MATLAB Engine API for Python."""
    print_step("Step 3: Installing MATLAB Engine for Python")
    engine_path = os.path.join(matlab_root, "extern", "engines", "python")
    
    if not os.path.exists(engine_path):
        print(f"❌ Error: Could not find the engine installation directory at {engine_path}")
        sys.exit(1)
    
    print("⏳ Running pip install ...")
    subprocess.run([sys.executable, "-m", "pip", "install", "."], cwd=engine_path, shell=True)
    print("✅ MATLAB Engine installed successfully!")

def setup_mcp_server():
    """Clone and build the MATLAB MCP Server from MathWorks GitHub."""
    print_step("Step 4: Downloading and building MATLAB MCP Server")
    target_dir = os.path.join(os.path.expanduser("~"), "Documents", "matlab-mcp-server")
    
    # Clean up existing directory if it exists to ensure a fresh build
    if os.path.exists(target_dir):
        print(f"🧹 Found existing directory, cleaning up: {target_dir}")
        shutil.rmtree(target_dir, ignore_errors=True)
        
    print("⏳ Cloning source code from GitHub...")
    subprocess.run(["git", "clone", "https://github.com/mathworks/matlab-mcp-server.git", target_dir], shell=True)
    
    print("⏳ Installing npm dependencies (this may take a minute)...")
    subprocess.run(["npm", "install"], cwd=target_dir, shell=True)
    
    print("⏳ Building the project...")
    subprocess.run(["npm", "run", "build"], cwd=target_dir, shell=True)
    
    dist_path = os.path.join(target_dir, "dist", "index.js")
    if os.path.exists(dist_path):
        print("✅ MCP Server built successfully!")
        return dist_path
    else:
        print("❌ Error: Build failed, 'dist/index.js' not found.")
        sys.exit(1)

def inject_claude_config(mcp_index_path, matlab_root):
    """Inject the MCP server configuration into Claude Desktop's config file."""
    print_step("Step 5: Injecting Claude Desktop configuration")
    config_path = os.path.expandvars(r"%APPDATA%\Claude\claude_desktop_config.json")
    
    # Read existing config or initialize a new one
    if os.path.exists(config_path):
        backup_path = config_path + ".backup"
        shutil.copy(config_path, backup_path)
        print(f"✅ Backed up original config to: {backup_path}")
        with open(config_path, 'r', encoding='utf-8') as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError:
                config = {"mcpServers": {}}
    else:
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        config = {"mcpServers": {}}

    if "mcpServers" not in config:
        config["mcpServers"] = {}
        
    # Construct node parameters (Converting Windows backslashes to forward slashes for JSON)
    matlab_exe = os.path.join(matlab_root, "bin", "matlab.exe").replace("\\", "/")
    node_script = mcp_index_path.replace("\\", "/")
    
    config["mcpServers"]["matlab"] = {
        "command": "node",
        "args": [node_script],
        "env": {
            "MATLAB_PATH": matlab_exe
        }
    }

    # Write the updated config back to the file
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    print("✅ Configuration successfully injected into Claude Desktop!")

def main():
    """Main execution flow."""
    print("🎉 Welcome to the MATLAB Vibe Coding 1-Click Setup Wizard (Windows) 🎉")
    
    matlab_root = find_matlab()
    check_dependencies()
    install_matlab_engine(matlab_root)
    mcp_index_path = setup_mcp_server()
    inject_claude_config(mcp_index_path, matlab_root)
    
    print_step("Installation Complete!")
    print("👇 Next steps:")
    print("1. Completely close and restart Claude Desktop.")
    print("2. Look for the hammer (tool) icon in your chat window to confirm the integration!")
    print("Happy Vibe Coding! 🚀")

if __name__ == "__main__":
    main()