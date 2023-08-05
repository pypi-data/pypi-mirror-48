<div class="footer-container">
    {% set copyright = owner.copyright|default(copyright, True)|default("Hive Solutions", True) %}
    {% set copyright_year = owner.copyright_year|default(copyright_year, True)|default("2014-2019", True) %}
    {% set copyright_url = owner.copyright_url|default(copyright_url, True)|default("http://hive.pt", True) %}
    &copy; Copyright {{ copyright_year }} by
    {% if copyright_url %}
        <a href="{{ copyright_url }}">{{ copyright }}</a>.<br/>
    {% else %}
        <span>{{ copyright }}</span>.<br/>
    {% endif %}
    {% if session.username %}<a href="{{ url_for('admin.show_account', username = session.username) }}">{{ session.username }}</a> // <a href="{{ url_for('admin.logout') }}">logout</a><br/>{% endif %}
</div>
