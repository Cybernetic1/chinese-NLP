                // This function is specially for Chinese pinyin matching
                patterns: function( input, context ) {
                        var i, j, patternsList = [], rule, replacement,
                                $menu, $li, $ul,
                                $element = this.$element,
                                $selector = $element.data('imeselector').$imeSetting,
                                selection = [], result = null;

                        patternsList = this.inputmethod.patternsList;
                        
                        // Find the rule of longest match
                        for ( i = 0; i < patternsList.length; i++ ) {
                                rule = patternsList[i];

                                if (input.match(rule[0])) {
                                        result = rule;
                                        selection.push(result.slice( -1 )[0]);
                                }
                        }

                        if (result == null)
                                // No matches, return the input
                                return input;

                        // Last item in the rule.
                        // It can also be a function, because the replace
                        // method can have a function as the second argument.
                        replacement = selection[0].slice( -1 )[0];

                        // Create selection menu
                        $menu = $('.ime-autocomplete', $selector);

                        if(!$menu.length) {
                                $menu = $('<div class="ime-autocomplete"></div>');
                                $ul = $('<ul></ul>');
                                $ul.appendTo($menu);
                                $selector.append($menu);
                        } else {
                                $ul = $('ul', $menu);

                                // Reset menu
                                $ul.empty();
                                $('li', $ul).navigate('destroy');
                        }

                        for(j = 0; j < selection.length; j++) {
                                $li = $('<li></li>');
                                $li.appendTo($ul)
                                        .text(selection[j])
                                        .data('replacement', selection[j]);
                        }

                        // Initialize jquery.navigate
                        $('ul li', $menu).not('.nokeyboard').navigate({
        wrap: true
      }).click(function(){
              var $input = $element;
              var val = $input.val();
              var newReplacement = $(this).data('replacement');
              var pos = val.lastIndexOf(replacement);

              // Reset
              $('li', $ul).navigate('destroy');
              $menu.remove();
              $input.val( val.substr(0, pos) + newReplacement ).focus();
      });

                        // Positioning the menu
                        var selectorPosition = $selector.position();

                        // Input string match test
                        return input.replace( result[0], replacement );
                }
