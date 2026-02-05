from fasthtml.common import *
import requests
from io import BytesIO

app, rt = fast_app()

# =========================
# HOME PAGE
# =========================
@rt("/")
def get():
    return Html(
        Head(
            Title("O-Ring Defect Detection | AI-Powered Quality Control"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Link(href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap", rel="stylesheet"),
            Style("""
                @keyframes gradientShift {
                    0%, 100% { transform: translate(0, 0) scale(1); }
                    33% { transform: translate(3%, -3%) scale(1.05); }
                    66% { transform: translate(-3%, 3%) scale(1.05); }
                }
                
                @keyframes float {
                    0%, 100% { transform: translateY(0px) rotate(0deg); }
                    50% { transform: translateY(-15px) rotate(2deg); }
                }
                
                @keyframes glow {
                    0%, 100% { box-shadow: 0 0 20px rgba(0, 255, 170, 0.3), 0 0 40px rgba(0, 255, 170, 0.15); }
                    50% { box-shadow: 0 0 35px rgba(0, 255, 170, 0.5), 0 0 60px rgba(0, 255, 170, 0.25); }
                }
                
                @keyframes slideInFromTop {
                    from {
                        opacity: 0;
                        transform: translateY(-40px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                
                @keyframes slideInFromBottom {
                    from {
                        opacity: 0;
                        transform: translateY(40px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                
                @keyframes scaleIn {
                    from {
                        opacity: 0;
                        transform: scale(0.92);
                    }
                    to {
                        opacity: 1;
                        transform: scale(1);
                    }
                }
                
                @keyframes shimmer {
                    0% { background-position: -1000px 0; }
                    100% { background-position: 1000px 0; }
                }
                
                @keyframes pulse {
                    0%, 100% { opacity: 1; }
                    50% { opacity: 0.6; }
                }
                
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                
                body {
                    font-family: 'Space Mono', monospace;
                    background: #0a0d14;
                    min-height: 100vh;
                    padding: 2rem 1rem;
                    position: relative;
                    overflow-x: hidden;
                    color: #ffffff;
                }
                
                body::before {
                    content: '';
                    position: fixed;
                    top: -50%;
                    left: -50%;
                    right: -50%;
                    bottom: -50%;
                    background: 
                        radial-gradient(circle at 25% 25%, rgba(0, 255, 170, 0.12) 0%, transparent 50%),
                        radial-gradient(circle at 75% 75%, rgba(138, 43, 226, 0.08) 0%, transparent 50%),
                        radial-gradient(circle at 50% 50%, rgba(0, 191, 255, 0.06) 0%, transparent 50%);
                    animation: gradientShift 25s ease infinite;
                    pointer-events: none;
                    z-index: 0;
                }
                
                body::after {
                    content: '';
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background-image: 
                        repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0, 255, 170, 0.03) 2px, rgba(0, 255, 170, 0.03) 4px);
                    pointer-events: none;
                    z-index: 1;
                    opacity: 0.4;
                }
                
                .container {
                    max-width: 1100px;
                    margin: 0 auto;
                    position: relative;
                    z-index: 2;
                }
                
                .header {
                    text-align: center;
                    margin-bottom: 3rem;
                    animation: slideInFromTop 0.9s cubic-bezier(0.16, 1, 0.3, 1);
                }
                
                .badge {
                    display: inline-block;
                    padding: 0.6rem 1.5rem;
                    background: rgba(0, 255, 170, 0.08);
                    border: 2px solid rgba(0, 255, 170, 0.3);
                    border-radius: 0;
                    color: #00ffaa;
                    font-size: 0.75rem;
                    font-weight: 700;
                    letter-spacing: 0.15em;
                    text-transform: uppercase;
                    margin-bottom: 1.5rem;
                    backdrop-filter: blur(10px);
                    animation: float 4s ease-in-out infinite;
                    font-family: 'Space Mono', monospace;
                }
                
                h1 {
                    font-family: 'Syne', sans-serif;
                    font-size: 4rem;
                    font-weight: 800;
                    background: linear-gradient(135deg, #ffffff 0%, #00ffaa 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                    margin-bottom: 1rem;
                    letter-spacing: -0.04em;
                    line-height: 1;
                    text-transform: uppercase;
                }
                
                .subtitle {
                    color: #8b95a5;
                    font-size: 1rem;
                    font-weight: 400;
                    line-height: 1.6;
                    max-width: 550px;
                    margin: 0 auto;
                    letter-spacing: 0.02em;
                }
                
                .main-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 2rem;
                    margin-bottom: 2rem;
                }
                
                .card {
                    background: rgba(15, 20, 30, 0.7);
                    border: 2px solid rgba(0, 255, 170, 0.15);
                    border-radius: 0;
                    padding: 2.5rem;
                    backdrop-filter: blur(20px);
                    box-shadow: 
                        0 20px 40px rgba(0, 0, 0, 0.4),
                        inset 0 1px 0 rgba(255, 255, 255, 0.03);
                    animation: scaleIn 0.7s cubic-bezier(0.16, 1, 0.3, 1) backwards;
                    position: relative;
                    overflow: hidden;
                    height: 100%;
                    display: flex;
                    flex-direction: column;
                }
                
                .card::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: -100%;
                    width: 200%;
                    height: 100%;
                    background: linear-gradient(
                        90deg,
                        transparent,
                        rgba(0, 255, 170, 0.05),
                        transparent
                    );
                    animation: shimmer 4s infinite;
                }
                
                .card.left {
                    animation-delay: 0s;
                }
                
                .card.right {
                    animation-delay: 0.15s;
                }
                
                .section-title {
                    font-family: 'Syne', sans-serif;
                    font-size: 1.25rem;
                    font-weight: 700;
                    color: #00ffaa;
                    margin-bottom: 2rem;
                    letter-spacing: 0.05em;
                    text-transform: uppercase;
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                }
                
                .section-title::before {
                    content: '';
                    width: 6px;
                    height: 6px;
                    background: #00ffaa;
                    box-shadow: 0 0 15px rgba(0, 255, 170, 0.8);
                }
                
                .upload-area {
                    border: 3px dashed rgba(0, 255, 170, 0.2);
                    border-radius: 0;
                    padding: 3rem 2rem;
                    text-align: center;
                    background: rgba(0, 255, 170, 0.02);
                    cursor: pointer;
                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    margin-bottom: 1.5rem;
                    position: relative;
                    flex: 1;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    min-height: 280px;
                }
                
                .upload-area::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: radial-gradient(circle at center, rgba(0, 255, 170, 0.08) 0%, transparent 70%);
                    opacity: 0;
                    transition: opacity 0.4s ease;
                }
                
                .upload-area:hover {
                    border-color: rgba(0, 255, 170, 0.6);
                    background: rgba(0, 255, 170, 0.05);
                    transform: translateY(-2px);
                }
                
                .upload-area:hover::before {
                    opacity: 1;
                }
                
                .upload-area.drag-over {
                    border-color: #00ffaa;
                    background: rgba(0, 255, 170, 0.1);
                    transform: scale(1.01);
                }
                
                .upload-icon {
                    width: 5rem;
                    height: 5rem;
                    background: rgba(0, 255, 170, 0.1);
                    border: 3px solid rgba(0, 255, 170, 0.3);
                    border-radius: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1.5rem;
                    font-size: 2.5rem;
                    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
                    position: relative;
                }
                
                .upload-area:hover .upload-icon {
                    transform: scale(1.1);
                    border-color: #00ffaa;
                    box-shadow: 0 0 30px rgba(0, 255, 170, 0.4);
                }
                
                .upload-text {
                    color: #e2e8f0;
                    font-size: 1rem;
                    margin-bottom: 0.75rem;
                    font-weight: 400;
                }
                
                .upload-text .browse-link {
                    color: #00ffaa;
                    text-decoration: none;
                    font-weight: 700;
                    position: relative;
                    border-bottom: 2px solid transparent;
                    transition: all 0.3s ease;
                }
                
                .upload-text .browse-link:hover {
                    border-bottom-color: #00ffaa;
                }
                
                .upload-formats {
                    color: #6b7280;
                    font-size: 0.875rem;
                    font-weight: 400;
                }
                
                .divider {
                    display: flex;
                    align-items: center;
                    text-align: center;
                    margin: 1.5rem 0;
                }
                
                .divider::before,
                .divider::after {
                    content: '';
                    flex: 1;
                    height: 2px;
                    background: rgba(0, 255, 170, 0.15);
                }
                
                .divider span {
                    padding: 0 1.25rem;
                    color: #6b7280;
                    font-size: 0.75rem;
                    font-weight: 700;
                    letter-spacing: 0.1em;
                    text-transform: uppercase;
                }
                
                .camera-button {
                    width: 100%;
                    padding: 1.25rem 1.5rem;
                    border: 2px solid rgba(0, 255, 170, 0.2);
                    border-radius: 0;
                    background: rgba(0, 255, 170, 0.03);
                    cursor: pointer;
                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    position: relative;
                    overflow: hidden;
                    backdrop-filter: blur(10px);
                }
                
                .camera-button:hover {
                    background: rgba(0, 255, 170, 0.08);
                    border-color: rgba(0, 255, 170, 0.5);
                    transform: translateY(-2px);
                }
                
                .camera-button:active {
                    transform: translateY(0);
                }
                
                .camera-icon {
                    width: 3rem;
                    height: 3rem;
                    background: rgba(0, 255, 170, 0.1);
                    border: 2px solid rgba(0, 255, 170, 0.3);
                    border-radius: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1.5rem;
                    flex-shrink: 0;
                    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
                }
                
                .camera-button:hover .camera-icon {
                    transform: scale(1.1);
                }
                
                .camera-text {
                    flex: 1;
                    text-align: left;
                }
                
                .camera-title {
                    color: #f1f5f9;
                    font-size: 1rem;
                    font-weight: 700;
                    display: block;
                    margin-bottom: 0.25rem;
                    text-transform: uppercase;
                    letter-spacing: 0.03em;
                }
                
                .camera-subtitle {
                    color: #8b95a5;
                    font-size: 0.875rem;
                    display: block;
                    font-weight: 400;
                }
                
                .model-grid {
                    display: flex;
                    flex-direction: column;
                    gap: 1rem;
                    flex: 1;
                }
                
                .model-card {
                    border: 2px solid rgba(0, 255, 170, 0.2);
                    border-radius: 0;
                    padding: 1.5rem;
                    cursor: pointer;
                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    background: rgba(0, 255, 170, 0.03);
                    display: flex;
                    align-items: center;
                    gap: 1.25rem;
                    position: relative;
                    overflow: hidden;
                    backdrop-filter: blur(10px);
                }
                
                .model-card::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: rgba(0, 255, 170, 0.05);
                    opacity: 0;
                    transition: opacity 0.4s ease;
                }
                
                .model-card:hover {
                    border-color: rgba(0, 255, 170, 0.5);
                    transform: translateX(4px);
                }
                
                .model-card:hover::before {
                    opacity: 1;
                }
                
                .model-card.selected {
                    border-color: #00ffaa;
                    background: rgba(0, 255, 170, 0.1);
                    box-shadow: 
                        0 0 0 4px rgba(0, 255, 170, 0.1),
                        inset 0 0 0 1px rgba(0, 255, 170, 0.3);
                    animation: glow 2s ease-in-out infinite;
                }
                
                .model-card.selected::before {
                    opacity: 1;
                }
                
                .model-card.selected::after {
                    content: '✓';
                    position: absolute;
                    top: 1rem;
                    right: 1rem;
                    width: 2rem;
                    height: 2rem;
                    background: #00ffaa;
                    color: #0a0d14;
                    border-radius: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1rem;
                    font-weight: 900;
                    box-shadow: 0 0 20px rgba(0, 255, 170, 0.6);
                }
                
                .model-icon {
                    width: 3rem;
                    height: 3rem;
                    background: rgba(0, 255, 170, 0.1);
                    border: 2px solid rgba(0, 255, 170, 0.3);
                    border-radius: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1.5rem;
                    flex-shrink: 0;
                    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
                    position: relative;
                    z-index: 1;
                }
                
                .model-card:hover .model-icon {
                    transform: scale(1.1);
                }
                
                .model-card.selected .model-icon {
                    background: rgba(0, 255, 170, 0.2);
                    border-color: #00ffaa;
                    box-shadow: 0 0 20px rgba(0, 255, 170, 0.4);
                }
                
                .model-info {
                    flex: 1;
                    position: relative;
                    z-index: 1;
                }
                
                .model-name {
                    color: #f1f5f9;
                    font-size: 1rem;
                    font-weight: 700;
                    display: block;
                    margin-bottom: 0.25rem;
                    text-transform: uppercase;
                    letter-spacing: 0.03em;
                }
                
                .model-desc {
                    color: #8b95a5;
                    font-size: 0.875rem;
                    line-height: 1.5;
                    font-weight: 400;
                }
                
                .analyze-section {
                    animation: slideInFromBottom 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.3s backwards;
                }
                
                .analyze-btn {
                    width: 100%;
                    padding: 1.5rem 2rem;
                    background: rgba(71, 85, 105, 0.3);
                    color: #6b7280;
                    border: 2px solid rgba(71, 85, 105, 0.3);
                    border-radius: 0;
                    font-size: 1rem;
                    font-weight: 700;
                    cursor: not-allowed;
                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 0.75rem;
                    position: relative;
                    overflow: hidden;
                    letter-spacing: 0.08em;
                    text-transform: uppercase;
                    font-family: 'Space Mono', monospace;
                }
                
                .analyze-btn::before {
                    content: '';
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    width: 0;
                    height: 0;
                    border-radius: 0;
                    background: rgba(255, 255, 255, 0.1);
                    transform: translate(-50%, -50%);
                    transition: width 0.6s, height 0.6s;
                }
                
                .analyze-btn.active {
                    background: #00ffaa;
                    color: #0a0d14;
                    cursor: pointer;
                    border-color: #00ffaa;
                    box-shadow: 0 0 40px rgba(0, 255, 170, 0.5);
                }
                
                .analyze-btn.active:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 0 50px rgba(0, 255, 170, 0.7);
                }
                
                .analyze-btn.active:hover::before {
                    width: 500px;
                    height: 500px;
                }
                
                .analyze-btn.active:active {
                    transform: translateY(-1px);
                }
                
                .footer {
                    text-align: center;
                    margin-top: 3rem;
                    color: #6b7280;
                    font-size: 0.875rem;
                    font-weight: 400;
                    animation: slideInFromBottom 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.5s backwards;
                }
                
                .footer::before {
                    content: '⚡';
                    margin-right: 0.5rem;
                    color: #00ffaa;
                }
                
                #video {
                    width: 100%;
                    max-height: 350px;
                    object-fit: contain;
                    border-radius: 0;
                    margin-top: 1.5rem;
                    display: none;
                    border: 2px solid rgba(0, 255, 170, 0.3);
                    background: rgba(15, 20, 30, 0.6);
                }
                
                #video.active {
                    display: block;
                    animation: scaleIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
                }
                
                .preview-container {
                    display: none;
                    margin-top: 1.5rem;
                    animation: scaleIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
                }
                
                .preview-image {
                    width: 100%;
                    max-height: 350px;
                    object-fit: contain;
                    border-radius: 0;
                    margin-bottom: 1rem;
                    border: 2px solid rgba(0, 255, 170, 0.2);
                    background: rgba(15, 20, 30, 0.6);
                }
                
                .preview-info {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    padding: 1rem 1.25rem;
                    background: rgba(15, 20, 30, 0.8);
                    border-radius: 0;
                    border: 2px solid rgba(0, 255, 170, 0.15);
                    backdrop-filter: blur(10px);
                }
                
                .preview-filename {
                    font-size: 0.875rem;
                    color: #e2e8f0;
                    font-weight: 400;
                    flex: 1;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    white-space: nowrap;
                    margin-right: 1rem;
                }
                
                .remove-btn {
                    background: #ff3366;
                    color: white;
                    border: none;
                    padding: 0.5rem 1rem;
                    border-radius: 0;
                    font-size: 0.75rem;
                    font-weight: 700;
                    cursor: pointer;
                    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                    flex-shrink: 0;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                    font-family: 'Space Mono', monospace;
                }
                
                .remove-btn:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 15px rgba(255, 51, 102, 0.4);
                }
                
                .remove-btn:active {
                    transform: translateY(0);
                }
                
                .results {
                    margin-top: 2.5rem;
                }
                
                .result-item {
                    background: rgba(15, 20, 30, 0.8);
                    border: 2px solid rgba(0, 255, 170, 0.2);
                    border-radius: 0;
                    padding: 2rem;
                    margin-bottom: 1.5rem;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
                    animation: slideInFromBottom 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
                    position: relative;
                    overflow: hidden;
                    backdrop-filter: blur(20px);
                }
                
                .result-item::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 6px;
                    height: 100%;
                    background: #00ffaa;
                    box-shadow: 0 0 20px rgba(0, 255, 170, 0.8);
                }
                
                .result-model {
                    font-size: 0.75rem;
                    font-weight: 700;
                    color: #00ffaa;
                    text-transform: uppercase;
                    margin-bottom: 1rem;
                    letter-spacing: 0.15em;
                    display: inline-block;
                    padding: 0.375rem 0.875rem;
                    background: rgba(0, 255, 170, 0.1);
                    border-radius: 0;
                    border: 1px solid rgba(0, 255, 170, 0.3);
                }
                
                .result-prediction {
                    font-family: 'Syne', sans-serif;
                    font-size: 2rem;
                    font-weight: 800;
                    color: #ffffff;
                    margin-bottom: 0.5rem;
                    text-transform: uppercase;
                    letter-spacing: 0.02em;
                }
                
                .result-confidence {
                    font-size: 1rem;
                    color: #8b95a5;
                    font-weight: 400;
                }
                
                canvas {
                    display: none;
                }
                
                input[type="file"] {
                    display: none;
                }
                
                .status-card {
                    background: rgba(0, 255, 170, 0.1);
                    border: 2px solid rgba(0, 255, 170, 0.3);
                    border-radius: 0;
                    padding: 1rem 1.25rem;
                    margin-top: 1.5rem;
                    text-align: center;
                    display: none;
                    animation: scaleIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
                    backdrop-filter: blur(10px);
                }
                
                .status-text {
                    font-size: 0.875rem;
                    color: #00ffaa;
                    font-weight: 700;
                    letter-spacing: 0.05em;
                }
                
                @media (max-width: 768px) {
                    body { 
                        padding: 1.5rem 1rem; 
                    }
                    
                    h1 {
                        font-size: 2.5rem;
                    }
                    
                    .main-grid {
                        grid-template-columns: 1fr;
                        gap: 1.5rem;
                    }
                    
                    .card {
                        padding: 2rem;
                    }
                    
                    .upload-area {
                        padding: 2rem 1.5rem;
                        min-height: 220px;
                    }
                    
                    .preview-image,
                    #video {
                        max-height: 280px;
                    }
                }
                
                @keyframes spin {
                    to { transform: rotate(360deg); }
                }
                
                .analyze-btn.loading::after {
                    content: '';
                    width: 1rem;
                    height: 1rem;
                    border: 2px solid rgba(10, 13, 20, 0.3);
                    border-top-color: #0a0d14;
                    border-radius: 50%;
                    animation: spin 0.6s linear infinite;
                    margin-left: 0.5rem;
                }
            """)
        ),
        Body(
            Div(
                # Header
                Div(
                    Div("AI-Powered", cls="badge"),
                    H1("O-Ring Defect Detection"),
                    P("Advanced neural networks for precision quality control and defect analysis", cls="subtitle"),
                    cls="header"
                ),
                
                # Main Grid
                Div(
                    # Left Card - Upload Section
                    Div(
                        Div("Upload Image", cls="section-title"),
                        
                        Input(
                            type="file",
                            id="file-input",
                            accept="image/*",
                            onchange="handleFileSelect(event)"
                        ),
                        
                        Label(
                            Div(
                                Div("📤", cls="upload-icon"),
                                Div(
                                    Span("Drop image here, or "),
                                    A("browse", href="javascript:void(0)", cls="browse-link", 
                                      onclick="document.getElementById('file-input').click()"),
                                    cls="upload-text"
                                ),
                                Div("JPG, PNG, WebP supported", cls="upload-formats"),
                            ),
                            For="file-input",
                            id="upload-area",
                            cls="upload-area",
                            ondragover="event.preventDefault(); this.classList.add('drag-over');",
                            ondragleave="this.classList.remove('drag-over');",
                            ondrop="handleDrop(event)"
                        ),
                        
                        Div(
                            Img(id="preview-img", cls="preview-image"),
                            Div(
                                Span(id="file-name", cls="preview-filename"),
                                Button("Remove", onclick="clearUpload()", cls="remove-btn"),
                                cls="preview-info"
                            ),
                            id="preview-container",
                            cls="preview-container"
                        ),
                        
                        Div(
                            Div(Span("OR"), cls="divider"),
                            cls="divider"
                        ),
                        
                        Button(
                            Div("📷", cls="camera-icon"),
                            Div(
                                Span("Capture Live", cls="camera-title"),
                                Span("Use device camera", cls="camera-subtitle"),
                                cls="camera-text"
                            ),
                            onclick="startCamera()",
                            id="camera-btn",
                            cls="camera-button"
                        ),
                        
                        Video(id="video", autoplay=True, playsinline=True),
                        Canvas(id="canvas"),
                        
                        Div(
                            P("Frames captured: ", Span("0", id="count"), " / 2", cls="status-text"),
                            id="status-card",
                            cls="status-card"
                        ),
                        
                        cls="card left"
                    ),
                    
                    # Right Card - Model Selection
                    Div(
                        Div("Select AI Model", cls="section-title"),
                        Div(
                            Div(
                                Div("⚙️", cls="model-icon"),
                                Div(
                                    Span("CNN Model", cls="model-name"),
                                    Span("Good / Breakage Detection", cls="model-desc"),
                                    cls="model-info"
                                ),
                                onclick="selectModel('cnn', this)",
                                id="model-cnn",
                                cls="model-card selected"
                            ),
                            Div(
                                Div("⚡", cls="model-icon"),
                                Div(
                                    Span("YOLO Model", cls="model-name"),
                                    Span("Paregi / Pelise Detection", cls="model-desc"),
                                    cls="model-info"
                                ),
                                onclick="selectModel('yolo', this)",
                                id="model-yolo",
                                cls="model-card"
                            ),
                            cls="model-grid"
                        ),
                        cls="card right"
                    ),
                    
                    cls="main-grid"
                ),
                
                # Analyze Button
                Div(
                    Button(
                        "🚀 Analyze Image",
                        onclick="analyzeImage()",
                        id="analyze-btn",
                        cls="analyze-btn"
                    ),
                    cls="analyze-section"
                ),
                
                # Results
                Div(id="results", cls="results"),
                
                # Footer
                P("Powered by CNN and YOLO deep learning models", cls="footer"),
                
                cls="container"
            ),
            
            # OpenCV.js
            Script(src="https://docs.opencv.org/4.x/opencv.js"),
            
            # JavaScript
            Script("""
let uploadedFile = null;
let selectedModel = 'cnn';
let stream = null;
let sent = 0;
const MAX_FRAMES = 2;

function selectModel(model, element) {
    selectedModel = model;
    document.querySelectorAll('.model-card').forEach(card => {
        card.classList.remove('selected');
    });
    element.classList.add('selected');
    updateAnalyzeButton();
}

function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        displayFile(file);
    }
}

function handleDrop(event) {
    event.preventDefault();
    const uploadArea = document.getElementById('upload-area');
    uploadArea.classList.remove('drag-over');
    
    const file = event.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
        document.getElementById('file-input').files = event.dataTransfer.files;
        displayFile(file);
    }
}

function displayFile(file) {
    uploadedFile = file;
    const preview = document.getElementById('preview-img');
    const previewContainer = document.getElementById('preview-container');
    const fileName = document.getElementById('file-name');
    const uploadArea = document.getElementById('upload-area');
    
    const reader = new FileReader();
    reader.onload = (e) => {
        preview.src = e.target.result;
        fileName.textContent = file.name;
        previewContainer.style.display = 'block';
        uploadArea.style.display = 'none';
        updateAnalyzeButton();
    };
    reader.readAsDataURL(file);
}

function clearUpload() {
    uploadedFile = null;
    document.getElementById('file-input').value = '';
    document.getElementById('preview-container').style.display = 'none';
    document.getElementById('upload-area').style.display = 'flex';
    updateAnalyzeButton();
}

function updateAnalyzeButton() {
    const analyzeBtn = document.getElementById('analyze-btn');
    if (uploadedFile) {
        analyzeBtn.classList.add('active');
    } else {
        analyzeBtn.classList.remove('active');
    }
}

function analyzeImage() {
    if (!uploadedFile) return;
    
    const analyzeBtn = document.getElementById('analyze-btn');
    analyzeBtn.innerHTML = '🔄 Analyzing...';
    analyzeBtn.classList.remove('active');
    analyzeBtn.classList.add('loading');
    
    const form = new FormData();
    form.append('file', uploadedFile);
    form.append('model', selectedModel);
    
    fetch('/predict', { method: 'POST', body: form })
        .then(r => r.text())
        .then(html => {
            // Clear previous results and show only current prediction
            document.getElementById('results').innerHTML = html;
            analyzeBtn.innerHTML = '🚀 Analyze Image';
            analyzeBtn.classList.remove('loading');
            updateAnalyzeButton();
        })
        .catch(err => {
            console.error('Prediction failed:', err);
            analyzeBtn.innerHTML = '🚀 Analyze Image';
            analyzeBtn.classList.remove('loading');
            updateAnalyzeButton();
            alert('Analysis failed. Please try again.');
        });
}

function startCamera() {
    const btn = document.getElementById('camera-btn');
    const video = document.getElementById('video');
    const statusCard = document.getElementById('status-card');
    
    btn.disabled = true;
    btn.querySelector('.camera-title').textContent = 'Starting...';
    
    navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
        .then(s => {
            stream = s;
            video.srcObject = s;
            video.classList.add('active');
            statusCard.style.display = 'block';
            btn.querySelector('.camera-title').textContent = 'Active';
            video.onloadedmetadata = () => processFrame();
        })
        .catch(err => {
            btn.disabled = false;
            btn.querySelector('.camera-title').textContent = 'Capture Live';
            alert('Camera access denied or not available');
        });
}

function processFrame() {
    if (sent >= MAX_FRAMES) {
        stream.getTracks().forEach(t => t.stop());
        document.getElementById('video').classList.remove('active');
        document.getElementById('camera-btn').querySelector('.camera-title').textContent = 'Complete';
        return;
    }
    
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const video = document.getElementById('video');
    
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);
    
    if (detectOring(canvas)) {
        sendFrame(canvas);
        sent++;
        document.getElementById('count').innerText = sent;
    }
    
    setTimeout(processFrame, 800);
}

function detectOring(canvas) {
    if (typeof cv === 'undefined') return false;
    
    let src = cv.imread(canvas);
    let gray = new cv.Mat();
    let blur = new cv.Mat();
    let circles = new cv.Mat();
    
    cv.cvtColor(src, gray, cv.COLOR_RGBA2GRAY);
    cv.GaussianBlur(gray, blur, new cv.Size(9, 9), 2);
    cv.HoughCircles(
        blur,
        circles,
        cv.HOUGH_GRADIENT,
        1,
        blur.rows / 4,
        100,
        30,
        30,
        200
    );
    
    src.delete(); 
    gray.delete(); 
    blur.delete();
    
    if (circles.cols === 1) {
        circles.delete();
        return true;
    }
    
    circles.delete();
    return false;
}

function sendFrame(canvas) {
    canvas.toBlob(blob => {
        const form = new FormData();
        form.append('file', blob, 'frame.jpg');
        form.append('model', selectedModel);
        
        fetch('/predict', { method: 'POST', body: form })
            .then(r => r.text())
            .then(html => {
                // Clear previous results and show only current prediction
                document.getElementById('results').innerHTML = html;
            })
            .catch(err => {
                console.error('Prediction failed:', err);
            });
    }, 'image/jpeg');
}
            """)
        )
    )


# =========================
# PREDICTION ROUTE
# =========================
@rt("/predict")
async def post(file: UploadFile, model: str):
    if model == "cnn":
        api = "https://oring.onrender.com/predict"
        name = "CNN Model"
    else:
        api = "https://oring-2.onrender.com/predict"
        name = "YOLO Model"
    
    img = await file.read()
    files = {"file": ("frame.jpg", BytesIO(img), "image/jpeg")}
    
    try:
        r = requests.post(api, files=files, timeout=130)
        data = r.json()
        
        return Div(
            Div(name, cls="result-model"),
            Div(data['prediction'], cls="result-prediction"),
            Div(f"Confidence: {data['confidence']:.2%}", cls="result-confidence"),
            cls="result-item"
        )
    except Exception as e:
        return Div(
            Div(name, cls="result-model"),
            Div("Error", cls="result-prediction", style="color: #ff3366;"),
            Div(f"Failed to get prediction: {str(e)}", cls="result-confidence"),
            cls="result-item"
        )


serve()