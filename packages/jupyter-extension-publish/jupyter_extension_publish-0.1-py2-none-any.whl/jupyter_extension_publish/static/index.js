define([
  'base/js/namespace',
  'base/js/utils'
], function(Jupyter, utils) {
  function load_ipython_extension() {
    var handler = function () {
      console.log(Jupyter)
      var version =  prompt('버전명을 입력하세요')
      if (!version) {
        return;
      }
      Jupyter.notebook.save_checkpoint();
      utils.ajax({
        url: '/publish_notebook',
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify({
          version: version,
          nb_path: Jupyter.notebook.notebook_path
        })
      }).done(function() {
        console.log('success');
      }).fail(function(xhr) {
        if (xhr.status === 409) {
          alert('version is exists');
        }
      });
    };

    var action = {
      icon: 'fa-book', // a font-awesome class used on buttons, etc
      help    : 'publish notebook',
      help_index : 'zz',
      handler : handler
    };
    var prefix = 'jupyter_extension_publish';
    var action_name = 'publish_notebook';

    var full_action_name = Jupyter.actions.register(action, action_name, prefix);
    Jupyter.toolbar.add_buttons_group([full_action_name]);
  }

  return {
    load_ipython_extension: load_ipython_extension
  };
});
