"""Render wizard page with tabs (Status, Public URL, Auth, MCP) and logs."""

from __future__ import annotations

import html
import time

from bling_mcp.bling_auth.tokens import load_token
from bling_mcp.config import get_config
from bling_mcp.utils.logger import get_logger

logger = get_logger(__name__)

# In-memory UI logs (last 50)
_ui_logs: list[tuple[int, str, str]] = []  # (timestamp_ms, level, message)


def push_log(level: str, message: str) -> None:
    global _ui_logs
    _ui_logs.append((int(time.time() * 1000), level, message))
    if len(_ui_logs) > 50:
        _ui_logs = _ui_logs[-50:]


def get_logs() -> list[tuple[int, str, str]]:
    return list(_ui_logs)


def _is_local_url(url: str | None) -> bool:
    if not url:
        return True
    return "localhost" in url or "127.0.0.1" in url or "0.0.0.0" in url


def get_nav_status() -> dict[str, str]:
    config = get_config()
    tokens = load_token()
    is_configured = config.is_configured()
    bling_ready = bool(tokens and is_configured)
    public_url = config.effective_public_base_url
    public_ready = bool(public_url) and not _is_local_url(public_url)
    return {
        "status": "ok",
        "public": "ok" if public_ready else "pending",
        "auth": "ok" if bling_ready else "warning" if is_configured else "pending",
        "mcp": "ok" if (config.mcp_transport == "http") else "pending",
    }


def render_status_section() -> str:
    config = get_config()
    tokens = load_token()
    is_configured = config.is_configured()
    public_url = config.effective_public_base_url or "Nao configurada (local apenas)"
    public_is_local = _is_local_url(config.effective_public_base_url)
    bling_label = "Nao configurado"
    bling_status = "error"
    if tokens and is_configured:
        from datetime import datetime
        exp = datetime.utcfromtimestamp(tokens.expires_at / 1000)
        now_ms = int(time.time() * 1000)
        if now_ms > tokens.expires_at:
            bling_label = "Token expirado"
            bling_status = "error"
        else:
            bling_label = f"Autenticado (expira {exp.strftime('%Y-%m-%d %H:%M')} UTC)"
            bling_status = "success"
    elif is_configured:
        bling_label = "Nao autenticado"
        bling_status = "error"
    public_label = public_url if not public_is_local else "Nao configurada"
    public_status = "warning" if public_is_local else "success"
    mcp_status = "success" if config.mcp_transport == "http" else "info"
    mcp_label = "Ativo" if config.mcp_transport == "http" else "Desativado"
    return f"""
    <div class="section-header">
      <h1 class="section-title">Status</h1>
      <p class="section-subtitle">Visao geral do sistema</p>
    </div>
    <div class="card">
      <div class="card-title"><span>&#128202;</span> Status do Sistema</div>
      <div class="status-grid">
        <div class="status-item">
          <div class="status-icon success">&#10003;</div>
          <div class="status-details">
            <div class="status-label">Servidor</div>
            <div class="status-value">Rodando</div>
          </div>
        </div>
        <div class="status-item">
          <div class="status-icon {public_status}">{"&#10003;" if public_status == "success" else "!"}</div>
          <div class="status-details">
            <div class="status-label">URL Publica</div>
            <div class="status-value text-small">{html.escape(public_label[:50] + ("..." if len(public_label) > 50 else ""))}</div>
          </div>
        </div>
        <div class="status-item">
          <div class="status-icon {bling_status}">{"&#10003;" if bling_status == "success" else "&#10007;" if bling_status == "error" else "!"}</div>
          <div class="status-details">
            <div class="status-label">Bling</div>
            <div class="status-value">{html.escape(bling_label)}</div>
          </div>
        </div>
        <div class="status-item">
          <div class="status-icon {mcp_status}">{"&#10003;" if mcp_status == "success" else "-"}</div>
          <div class="status-details">
            <div class="status-label">MCP HTTP</div>
            <div class="status-value">{html.escape(mcp_label)}</div>
          </div>
        </div>
      </div>
    </div>"""


def render_public_section() -> str:
    config = get_config()
    public_url = config.effective_public_base_url or ""
    redirect_uri = config.effective_redirect_uri
    return f"""
    <div class="section-header">
      <h1 class="section-title">URL Publica</h1>
      <p class="section-subtitle">Configure PUBLIC_BASE_URL no ambiente para OAuth e MCP remoto</p>
    </div>
    <div class="card">
      <div class="card-title"><span>&#127760;</span> Configuracao</div>
      <div class="alert alert-info">
        <span class="alert-icon">&#128161;</span>
        <div>Este servidor nao gerencia tunnels. Use qualquer tunnel (Cloudflare, etc.) e defina PUBLIC_BASE_URL no .env.</div>
      </div>
      <div class="info-box">
        <div class="info-box-title">URL publica atual</div>
        <div class="info-box-content"><span class="code">{html.escape(public_url or "Nao configurada (local apenas)")}</span></div>
      </div>
      <div class="info-box text-small">
        <div class="info-box-title">Redirect URI (Bling)</div>
        <div class="info-box-content"><span class="code">{html.escape(redirect_uri)}</span></div>
      </div>
    </div>"""


def render_auth_section() -> str:
    config = get_config()
    local_url = f"http://localhost:{config.port}"
    is_configured = config.is_configured()
    tokens = load_token()
    redirect_uri = config.effective_redirect_uri
    public_url = config.effective_public_base_url or local_url

    # Calculate token expiry
    token_status = {"text": "N/A", "is_expired": True, "is_expiring_soon": False}
    if tokens and tokens.expires_at:
        now_ms = int(time.time() * 1000)
        time_left_ms = tokens.expires_at - now_ms
        time_left_hours = time_left_ms / (1000 * 60 * 60)

        if now_ms > tokens.expires_at:
            token_status = {"text": "Expirado", "is_expired": True, "is_expiring_soon": False}
        elif time_left_hours < 24:
            hours = int(time_left_hours)
            minutes = int((time_left_hours - hours) * 60)
            token_status = {
                "text": f"{hours}h {minutes}m",
                "is_expired": False,
                "is_expiring_soon": True
            }
        else:
            days = int(time_left_hours / 24)
            token_status = {
                "text": f"{days} dias",
                "is_expired": False,
                "is_expiring_soon": False
            }

    # Check if public URL might block OAuth (localhost check)
    auth_block_reason = ""
    if not _is_local_url(public_url) and _is_local_url(redirect_uri):
        auth_block_reason = "Redirect URI aponta para localhost mas URL publica esta configurada. Configure PUBLIC_BASE_URL corretamente."

    if tokens and is_configured:
        # Authenticated state
        body = f"""
        <div class="card">
          <div class="card-title"><span>&#10003;</span> Status da Autenticacao</div>
          <div class="alert alert-success">
            <span class="alert-icon">&#10003;</span>
            <div><strong>Autenticado com sucesso!</strong><br/>Sua conexao com o Bling esta ativa.</div>
          </div>
          <div class="info-box">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px;">
              <div>
                <div class="text-muted text-small">Status do Token</div>
                <div>
                  {"<span class='badge badge-error'>Expirado</span>" if token_status["is_expired"]
                   else f"<span class='badge badge-warning'>Expira em {token_status['text']}</span>" if token_status["is_expiring_soon"]
                   else f"<span class='badge badge-success'>Valido ({token_status['text']})</span>"}
                </div>
              </div>
              <div>
                <div class="text-muted text-small">Redirect URI</div>
                <div><span class="code text-small">{html.escape(redirect_uri)}</span></div>
              </div>
            </div>
          </div>
          <div class="btn-group">
            {"" if auth_block_reason else f'<a href="{local_url}/start" class="btn btn-primary">Reautenticar</a>'}
            <form method="POST" action="/bling/token/test" style="display: inline;">
              <button type="submit" class="btn btn-warning">Testar refresh do token</button>
            </form>
            <a href="/logout" class="btn btn-secondary">Logout</a>
          </div>
          {f'<div class="alert alert-warning mt-4"><span class="alert-icon">!</span><div>{html.escape(auth_block_reason)}</div></div>' if auth_block_reason else ''}
        </div>
        """
    elif not is_configured:
        # Not configured state - show configuration form
        body = f"""
        <div class="card">
          <div class="card-title"><span>&#128274;</span> Configurar Credenciais</div>
          <div class="alert alert-info">
            <span class="alert-icon">&#128161;</span>
            <div>
              Antes de comecar, cadastre um aplicativo no Bling:<br/>
              <span class="code">Configuracoes > Integracoes > Aplicativos</span><br/>
              <a href="https://developer.bling.com.br/aplicativos#fluxo-de-autoriza%C3%A7%C3%A3o" target="_blank" rel="noreferrer">Ver documentacao oficial</a>
            </div>
          </div>
          <form method="POST" action="/configure">
            <div class="form-group">
              <label class="form-label">Client ID</label>
              <input type="text" name="clientId" class="form-input" required placeholder="Encontre em Bling > Configuracoes > Integracoes" />
            </div>
            <div class="form-group">
              <label class="form-label">Client Secret</label>
              <input type="password" name="clientSecret" class="form-input" required placeholder="Senha do aplicativo" />
            </div>
            <button type="submit" class="btn btn-primary">Salvar Credenciais</button>
          </form>
        </div>
        """
    else:
        # Configured but not authenticated
        body = f"""
        <div class="card">
          <div class="card-title"><span>&#128274;</span> Configurar Credenciais</div>
          <div class="alert alert-warning">
            <span class="alert-icon">!</span>
            <div>Credenciais configuradas, mas ainda nao autenticado. Clique em "Autorizar" abaixo.</div>
          </div>
          {f'<div class="alert alert-error"><span class="alert-icon">&#10007;</span><div>{html.escape(auth_block_reason)}</div></div>' if auth_block_reason else ''}
          <div class="info-box mb-4">
            <div class="info-box-title">Redirect URI para o Bling</div>
            <div class="info-box-content">
              Configure esta URL no cadastro do aplicativo do Bling:<br/>
              <span class="code" style="display: block; margin-top: 8px; padding: 10px;">{html.escape(redirect_uri)}</span>
            </div>
          </div>
          {"" if auth_block_reason else f'<a href="{local_url}/start" class="btn btn-success">Autorizar com Bling</a>'}
          <a href="/logout" class="btn btn-secondary" style="margin-left: 10px;">Limpar Credenciais</a>
        </div>
        """

    # Add "How it works" section
    how_it_works = """
    <details style="margin-top: 20px;">
      <summary>&#128218; Como funciona a autenticacao</summary>
      <div>
        <ol class="text-muted" style="margin-left: 20px; line-height: 2;">
          <li>Cadastre um aplicativo no Bling e obtenha Client ID e Secret</li>
          <li>Configure a Redirect URI apontando para este servidor</li>
          <li>Clique em "Autorizar" - voce sera redirecionado ao Bling</li>
          <li>Autorize o aplicativo - o Bling redireciona de volta com um codigo</li>
          <li>O servidor troca o codigo por tokens de acesso</li>
          <li>Os tokens sao renovados automaticamente quando necessario</li>
        </ol>
      </div>
    </details>
    """

    return f"""
    <div class="section-header">
      <h1 class="section-title">Autenticacao Bling</h1>
      <p class="section-subtitle">Autenticacao OAuth com o Bling ERP</p>
    </div>
    {body}
    {how_it_works}
    """


def render_mcp_section() -> str:
    config = get_config()
    public_url = config.effective_public_base_url or f"http://localhost:{config.port}"
    mcp_url = f"{public_url.rstrip('/')}/mcp"
    return f"""
    <div class="section-header">
      <h1 class="section-title">MCP</h1>
      <p class="section-subtitle">Configuracao de clientes MCP</p>
    </div>
    <div class="card">
      <div class="card-title"><span>&#128268;</span> Endpoint HTTP</div>
      <p>Quando MCP_TRANSPORT for <code>http</code>, o MCP estara em:</p>
      <div class="code-block mt-2">{html.escape(mcp_url)}</div>
      <p class="mt-4">Para stdio, use <code>python -m bling_mcp</code> ou <code>bling-mcp</code> no cliente.</p>
    </div>"""


def render_logs_panel() -> str:
    logs = get_logs()
    from datetime import datetime
    lines = []
    for ts, level, msg in logs[-50:]:
        t = datetime.utcfromtimestamp(ts / 1000).strftime("%H:%M:%S")
        lines.append(f'<div class="log-entry {level}"><span class="log-timestamp">[{t}]</span>{level.upper()} {html.escape(msg)}</div>')
    content = "\n".join(lines) if lines else '<div class="text-muted">Sem logs ainda.</div>'
    return f'<div class="logs-panel"><div class="logs-header"><div class="logs-title">Logs</div></div><div class="logs-content">{content}</div></div>'


def get_main_content(active_tab: str) -> str:
    if active_tab == "status":
        return render_status_section()
    if active_tab == "public":
        return render_public_section()
    if active_tab == "auth":
        return render_auth_section()
    if active_tab == "mcp":
        return render_mcp_section()
    return render_status_section()
