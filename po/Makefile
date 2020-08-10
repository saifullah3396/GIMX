
all:
	

install:
	mkdir -p $(DESTDIR)/tmp/gimx/share/locale
	for translation in *.po; \
  do \
    po=$$(basename "$${translation}" .po); \
    mkdir -p $(DESTDIR)/tmp/gimx/share/locale/$$po/LC_MESSAGES; \
    msgfmt -o $(DESTDIR)/tmp/gimx/share/locale/$$po/LC_MESSAGES/gimx.mo $$po.po; \
  done

uninstall:
	$(RM) $(DESTDIR)/tmp/gimx/share/locale/*/LC_MESSAGES/gimx.mo

clean:
	