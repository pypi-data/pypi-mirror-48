## -*- coding: utf-8; -*-
<%inherit file="/master/view.mako" />

<%def name="extra_javascript()">
  ${parent.extra_javascript()}
  % if not use_buefy:
  <script type="text/javascript">
    % if not email.get_template('html'):
      $(function() {
          $('#preview-html').button('disable');
          $('#preview-html').attr('title', "There is no HTML template on file for this email.");
      });
    % endif
    % if not email.get_template('txt'):
      $(function() {
          $('#preview-txt').button('disable');
          $('#preview-txt').attr('title', "There is no TXT template on file for this email.");
      });
    % endif
  </script>
  % endif
</%def>

${parent.body()}

% if use_buefy:

    <script type="text/x-template" id="email-preview-tools-template">

    ${h.form(url('email.preview'))}
      ${h.csrf_token(request)}
      ${h.hidden('email_key', value=instance['key'])}

      <div class="field is-grouped">

        <div class="control">
          % if email.get_template('html'):
              <a class="button is-primary"
                 href="${url('email.preview')}?key=${instance['key']}&type=html"
                 target="_blank">
                Preview HTML
              </a>
          % else:
              <button class="button is-primary"
                      type="button"
                      title="There is no HTML template on file for this email."
                      disabled>
                Preview HTML
              </button>
          % endif
        </div>

        <div class="control">
        % if email.get_template('txt'):
            <a class="button is-primary"
               href="${url('email.preview')}?key=${instance['key']}&type=txt"
               target="_blank">
              Preview TXT
            </a>
        % else:
            <button class="button is-primary"
                    type="button"
                    title="There is no TXT template on file for this email."
                    disabled>
              Preview TXT
            </button>
        % endif
        </div>

        <div class="control">
          or
        </div>

        <div class="control">
          <input name="recipient" type="email" class="input" value="${request.user.email_address or ''}" />
        </div>

        <div class="control">
          <once-button type="is-primary"
                       native-type="submit"
                       text="Send Preview Email">
          </once-button>
        </div>

      </div><!-- field -->

    ${h.end_form()}
    </script>

    <script type="text/javascript">

      const EmailPreviewTools = {
          template: '#email-preview-tools-template'
      }

      Vue.component('email-preview-tools', EmailPreviewTools)

    </script>

    <div id="email-preview-tools-app">
      <email-preview-tools></email-preview-tools>
    </div>

    <script type="text/javascript">

      new Vue({
          el: '#email-preview-tools-app'
      })

    </script>

% else:
    ## not buefy; do traditional thing

    ${h.form(url('email.preview'), name='send-email-preview', class_='autodisable')}
      ${h.csrf_token(request)}
      ${h.hidden('email_key', value=instance['key'])}
      ${h.link_to("Preview HTML", '{}?key={}&type=html'.format(url('email.preview'), instance['key']), id='preview-html', class_='button', target='_blank')}
      ${h.link_to("Preview TXT", '{}?key={}&type=txt'.format(url('email.preview'), instance['key']), id='preview-txt', class_='button', target='_blank')}
      or
      ${h.text('recipient', value=request.user.email_address or '')}
      ${h.submit('send_{}'.format(instance['key']), value="Send Preview Email")}
    ${h.end_form()}

% endif
