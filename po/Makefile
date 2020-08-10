
all:
	

install:
	mkdir -p $(DESTDIR)/usr/local/share/locale
	for translation in *.po; \
  do \
    po=$$(basename "$${translation}" .po); \
    mkdir -p $(DESTDIR)/usr/local/share/locale/$$po/LC_MESSAGES; \
    msgfmt -o $(DESTDIR)/usr/local/share/locale/$$po/LC_MESSAGES/gimx.mo $$po.po; \
  done

uninstall:
	$(RM) $(DESTDIR)/usr/local/share/locale/*/LC_MESSAGES/gimx.mo

clean:
	