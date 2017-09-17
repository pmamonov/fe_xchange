#!/usr/bin/env ipython --pylab

from pickle import load
ea = load("ea.dump")
f = open("ea.dump")
ea = load(f)
ea
plot(ea)
ls
import Ea
fe3h = loadtxt("/home/piton/erg/mm/fe_xchange/lomo/fe3_01kcal/lambda1000/FE3_SOL_10-MTD-1.hills")
fe3h.shape
fe3v = zeros(-10,10,2001)
ip = linspace(-10,10,2001)
fe3v = 0*ip
for x in fe3h: fe3v += 0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
fe3h = loadtxt("/home/piton/erg/mm/fe_xchange/lomo/fe3_01kcal/lambda1000/FE3_SOL_10-MTD-1.hills")[::3]
fe3v = 0*ip
for x in fe3h: fe3v += 0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
plot(ip, fe3v)
plot(ip, -fe3v)
fe3h.shape
fe3v = 0*ip
for x in fe3h[:1600]: fe3v += 0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
fe2h = loadtxt("/home/piton/erg/mm/fe_xchange/lomo/fe2/01kcal/l1e3/FE2_SOL_10-MTD-1.hills")[::3]
fe2v = 0*ip
for x in fe2h: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
plot(ip, -fe3v)
plot(ip, fe2v)
clf()
fe2v = 0*ip
fe3v = 0*ip
for x in fe3h[:1600]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
for x in fe2h[:1600]: fe2v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
plot(ip, fe3v)
plot(ip, fe2v)
Ea.Ea?
Ea.Ea(fe3v, fe2v, 300)
fe2h.shape
fe2v = 0*ip
for x in fe2h[:1200]: fe2v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
fe2v = 0*ip
for x in fe2h[:1000]: fe2v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
fe2v = 0*ip
for x in fe2h[:1500]: fe2v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
fe3v = 0*ip
for x in fe3h[:1700]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
fe2v = 0*ip
for x in fe2h[:1700]: fe2v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
fe2v = 0*ip
for x in fe2h[:1600]: fe2v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
Ea.Ea(fe3v, fe2v, 300)
fe3v = 0*ip
for x in fe3h[:1750]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
for x in fe3h[:1800]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
fe3v = 0*ip
for x in fe3h[:1800]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
fe3v = 0*ip
for x in fe3h[:1750]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
fe3v = 0*ip
for x in fe3h[:1770]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
fe3v = 0*ip
for x in fe3h[:1770]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
for x in fe3h[:1780]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
fe3v = 0*ip
for x in fe3h[:1780]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
for x in fe3h[:1785]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
fe3v = 0*ip
for x in fe3h[:1785]: fe3v += -0.1*exp(-0.5*((ip/27.212 - x)/0.011)**2)
Ea.Ea(fe3v, fe2v, 300)
clf()
plot(ip, fe2v)
plot(ip, fe3v)
T = arange(270,310,1)
k_T = map(lambda x: Ea.Ea(fe2v,fe3v,x), T)
clf()
plot(T, k_T-k_T.min())
plot(T, log10(k_T)-min(log10(k_T)))
clf()
plot(1./T, log10(k_T)-min(log10(k_T)))
k_T = map(lambda x: (exp(-fe2v/2e-3/x) * exp(-fe3v/2e-3/x)/(exp(-fe2v/2e-3/x)).sum()/(exp(-fe3v/2e-3/x)).sum()).sum(), T)
x=273; k_273 = (exp(-fe2v/2e-3/x) * exp(-fe3v/2e-3/x)/(exp(-fe2v/2e-3/x)).sum()/(exp(-fe3v/2e-3/x)).sum()).sum()
plot(1/T, log10(array(k_T)/k_273))
clf()
plot(1/T, log10(array(k_T)/k_273))
plot(1./T, log10(array(k_T)/k_273))
clf()
plot(1./T, log10(array(k_T)/k_273))
k_exp = loadtxt("Ea.exp")
pwd
ls
pwd
Ea.exp
Ea.exp?
Texp = array([0, 7.3, 14.7, 21.6])+273.5
kexp = array([0.87, 1.4, 2.2, 3.3])
plot(1./Texp, log10(kexp/k[0]), 'o')
plot(1./Texp, log10(kexp/kexp[0]), 'o')
clf()
plot(1./Texp, log10(kexp/kexp[0]), 'ok')
x=273.5; k_273 = (exp(-fe2v/2e-3/x) * exp(-fe3v/2e-3/x)/(exp(-fe2v/2e-3/x)).sum()/(exp(-fe3v/2e-3/x)).sum()).sum()
plot(1./T, log10(array(k_T)/k_273))
clf()
plot(1./Texp, log10(kexp/kexp[0]), 'ok', label=u"Экспериментальные данные")
plot(1./T, log10(array(k_T)/k_273)б )
plot(1./T, log10(array(k_T)/k_273), label=u'Результаты моделирования' )
plot(1./T, log10(array(k_T)/k_273), '-k', linewidth=0.1,label=u'Результаты моделирования' )
plot(1./T, log10(array(k_T)/k_273), '-k', linewidth=0.5,label=u'Результаты моделирования' )
plot(1./T, log10(array(k_T)/k_273), '-k', linewidth=1,label=u'Результаты моделирования' )
plot(1./T, log10(array(k_T)/k_273), '-k', linewidth=1.5,label=u'Результаты моделирования' )
legend()
clf()
plot(1./Texp, log10(kexp/kexp[0]), 'ok', label=u"Экспериментальные данные")
plot(1./T, log10(array(k_T)/k_273), '-k', linewidth=1.5,label=u'Результаты моделирования' )
legend()
ylabel("$lg(\frac{k_T}{k_{273.5}})$")
ylabel("$lg(\\frac{k_T}{k_{273.5}})$")
ylabel("$lg(\\frac{k_T}{k_{273.5}})$", fonsize=12)
ylabel("$lg(\\frac{k_T}{k_{273.5}})$", fontsize=12)
ylabel("$lg(\\frac{k_T}{k_{273.5}})$", fontsize=16)
ylabel("$lg(\\frac{k_T}{k_{273.5}})$", fontsize=18)
T
Tlab = range(270,320,10)
xticks(1./Tlab, map(lambda x: str(x), Tlab))
xticks(1./array(Tlab), map(lambda x: str(x), Tlab))
xticks(1./array(Tlab), map(lambda x: "1/%.0f"%(x), Tlab))
xlabel('$T^{-1}, K$')
xlabel('$T^{-1}, K$', fontsize=18)
xticks(1./array(Tlab), map(lambda x: "1/%.0f"%(x), Tlab), fontsize=16)
yticks(linspace(0,1,6), fontsize=16)
savefig('/home/piton/docs/fe_xchange/final/mamonov/fig-4.png')
%history
%history -f plot_k_vs_T.py
