## Algebraic and Number Theoretic Algorithms
### Algorithm: Factoring
- **Speedup**: Superpolynomial
- **Description**: Given an n-bit integer, find the prime factorization. The quantum algorithm of Peter Shor solves this in $\widetilde{O} (n^3)$ time [[82](#82), [125](#125)]. The fastest known classical algorithm for integer factorization is the general number field sieve, which is believed to run in time $2^{\widetilde{O}(n^{1/3})}$. The best rigorously proven upper bound on the classical complexity of factoring is $O(2^{n/4+o(1)})$ via the Pollard-Strassen algorithm [[252](#252),[362](#362)]. Shor's factoring algorithm breaks RSA public-key encryption and the closely related quantum algorithms for discrete logarithms break the DSA and ECDSA digital signature schemes and the Diffie-Hellman key-exchange protocol. A quantum algorithm even faster than Shor's for the special case of factoring âsemiprimesâ, which are widely used in cryptography, is given in [[271](#271)]. If small factors exist, Shor's algorithm can be beaten by a quantum algorithm using Grover search to speed up the elliptic curve factorization method [[366](#366)]. Additional optimized versions of Shor's algorithm are given in [[384](#384),[386](#386)]. There are proposed classical public-key cryptosystems not believed to be broken by quantum algorithms, cf. [[248](#248)]. At the core of Shor's factoring algorithm is order finding, which can be reduced to the Abelian hidden subgroup problem, which is solved using the quantum Fourier transform. A number of other problems are known to reduce to integer factorization including the membership problem for matrix groups over fields of odd order [[253](#253)], and certain diophantine problems relevant to the synthesis of quantum circuits [[254](#254)].

---

### Algorithm: Discrete-log
- **Speedup**: Superpolynomial
- **Description**: We are given three n-bit numbers a, b, and N, with the promise that $b = a^s \mod N$ for some s. The task is to find s. As shown by Shor [[82](#82)], this can be achieved on a quantum computer in poly(n) time. The fastest known classical algorithm requires time superpolynomial in n. By similar techniques to those in [[82](#82)], quantum computers can solve the discrete logarithm problem on elliptic curves, thereby breaking elliptic curve cryptography [[109](#109),[14](#14)]. A further optimization to Shor's algorithm is given in [ [385]]. The superpolynomial quantum speedup has also been extended to the discrete logarithm problem on semigroups [[203](#203),[204](#204)]. See also Abelian Hidden Subgroup.

---

### Algorithm: Pell's Equation
- **Speedup**: Superpolynomial
- **Description**: Given a positive nonsquare integer d, Pell's equation is $x^2 - d y^2 = 1$. For any such d there are infinitely many pairs of integers (x,y) solving this equation. Let $(x_1,y_1)$ be the pair that minimizes $x+y\sqrt{d}$. If d is an n-bit integer (i.e. $0 \leq d \lt 2^n$ ), $(x_1,y_1)$ may in general require exponentially many bits to write down. Thus it is in general impossible to find $(x_1,y_1)$ in polynomial time. Let $R = \log(x_1+y_1 \sqrt{d})$. $\lfloor R \rceil$ uniquely identifies $(x_1,y_1)$. As shown by Hallgren [[49](#49)], given a n-bit number d, a quantum computer can find $\lfloor R \rceil$ in poly(n) time. No polynomial time classical algorithm for this problem is known. Factoring reduces to this problem. This algorithm breaks the Buchman-Williams cryptosystem. See also Abelian hidden subgroup.

---

### Algorithm: Principal Ideal
- **Speedup**: Superpolynomial
- **Description**: We are given an n-bit integer d and an invertible ideal I of the ring $\mathbb{Z}[\sqrt{d}]$. I is a principal ideal if there exists $\alpha \in \mathbb{Q}(\sqrt{d})$ such that $I = \alpha \mathbb{Z}[\sqrt{d}]$. $\alpha$ may be exponentially large in d. Therefore Îą cannot in general even be written down in polynomial time. However, $\lfloor \log \alpha \rceil$ uniquely identifies $\alpha$. The task is to determine whether I is principal and if so find $\lfloor \log \alpha \rceil$. As shown by Hallgren, this can be done in polynomial time on a quantum computer [[49](#49)]. A modified quantum algorithm for this problem using fewer qubits was given in [[131](#131)]. A quantum algorithm solving the principal ideal problem in number fields of arbitrary degree (i.e. scaling polynomially in the degree) was subsequently given in [[329](#329)]. Factoring reduces to solving Pell's equation, which reduces to the principal ideal problem. Thus the principal ideal problem is at least as hard as factoring and therefore is probably not in P. See also Abelian hidden subgroup.

---

### Algorithm: Unit Group
- **Speedup**: Superpolynomial
- **Description**: The number field $\mathbb{Q}(\theta)$ is said to be of degree d if the lowest degree polynomial of which $\theta$ is a root has degree d. The set $\mathcal{O}$ of elements of $\mathbb{Q}(\theta)$ which are roots of monic polynomials in $\mathbb{Z}[x]$ forms a ring, called the ring of integers of $\mathbb{Q}(\theta)$. The set of units (invertible elements) of the ring $\mathcal{O}$ form a group denoted $\mathcal{O}^*$. As shown by Hallgren [[50](#50)], and independently by Schmidt and Vollmer [[116](#116)], for any $\mathbb{Q}(\theta)$ of fixed degree, a quantum computer can find in polynomial time a set of generators for $\mathcal{O}^*$ given a description of $\theta$. No polynomial time classical algorithm for this problem is known. Hallgren and collaborators subsequently discovered how to achieve polynomial scaling in the degree [[213](#213)]. See also [[329](#329)]. The algorithms rely on solving Abelian hidden subgroup problems over the additive group of real numbers.

---

### Algorithm: Class Group
- **Speedup**: Superpolynomial
- **Description**: The number field $\mathbb{Q}(\theta)$ is said to be of degree d if the lowest degree polynomial of which $\theta$ is a root has degree d. The set $\mathcal{O}$ of elements of $\mathbb{Q}(\theta)$  which are roots of monic polynomials in $\mathbb{Z}[x]$ forms a ring, called the ring of integers of $\mathbb{Q}(\theta)$. For a ring, the ideals modulo the prime ideals form a group called the class group. As shown by Hallgren [[50](#50)], a quantum computer can find in a set of generators for the class group of the ring of integers of any constant degree number field, given a description of $\theta$ in time poly(log($| \mathcal{O} |$)). An improved quantum algorithm, whose runtime is also polynomial in d was subsequently given in [[329](#329)]. No polynomial time classical algorithm for these problems are known. See also Abelian hidden subgroup.

---

### Algorithm: Gauss Sums
- **Speedup**: Superpolynomial
- **Description**: Let $\mathbb{F}_q$ be a finite field. The elements other than zero of $\mathbb{F}_q$ form a group $\mathbb{F}_q^\times$ under multiplication, and the elements of $\mathbb{F}_q$ form an (Abelian but not necessarily cyclic) group $\mathbb{F}_q^+$ under addition. We can choose some character $\chi^\times$ of $\mathbb{F}_q^\times$ and some character $\chi^+$ of $\mathbb{F}_q^+$. The corresponding Gauss sum is the inner product of these characters: $\sum_{x \neq 0 \in \mathbb{F}_q} \chi^+(x) \chi^\times(x)$ As shown by van Dam and Seroussi [[90](#90)], Gauss sums can be estimated to polynomial precision on a quantum computer in polynomial time. Although a finite ring does not form a group under multiplication, its set of units does. Choosing a representation for the additive group of the ring, and choosing a representation for the multiplicative group of its units, one can obtain a Gauss sum over the units of a finite ring. These can also be estimated to polynomial precision on a quantum computer in polynomial time [[90](#90)]. No polynomial time classical algorithm for estimating Gauss sums is known. Discrete log reduces to Gauss sum estimation [[90](#90)]. Certain partition functions of the Potts model can be computed by a polynomial-time quantum algorithm related to Gauss sum estimation [[47](#47)].

---

### Algorithm:Solving Exponential Congruences
- **Speedup**:Polynomial
- **Description**: We are given $a,b,c,f,g \in \mathbb{F}_q$. We must find integers $x,y$ such that $a f^x + b g^y = c$. As shown in [[111](#111)], quantum computers can solve this problem in $\widetilde{O}(q^{3/8})$ time whereas the best classical algorithm requires $\widetilde{O}(q^{9/8})$ time. The quantum algorithm of [[111](#111)] is based on the quantum algorithms for discrete logarithms and searching.

---

### Algorithm: Matrix Elements of Group Representations
- **Speedup**: Superpolynomial
- **Description**: All representations of finite groups and compact linear groups can be expressed as unitary matrices given an appropriate choice of basis. Conjugating the regular representation of a group by the quantum Fourier transform circuit over that group yields a direct sum of the group's irreducible representations. Thus, the efficient quantum Fourier transform over the symmetric group [[196](#196)], together with the Hadamard test, yields a fast quantum algorithm for additively approximating individual matrix elements of the arbitrary irreducible representations of $S_n$. Similarly, using the quantum Schur transform [[197](#197)], one can efficiently approximate matrix elements of the irreducible representations of SU(n) that have polynomial weight. Direct implementations of individual irreducible representations for the groups U(n), SU(n), SO(n), and $A_n$ by efficient quantum circuits are given in [[106](#106)]. Instances that appear to be exponentially hard for known classical algorithms are also identified in [[106](#106)].

---

### Algorithm: Verifying Matrix Products
- **Speedup**: Polynomial
- **Description**: Given three $n \times n$ matrices, A,B, and C, the matrix product verification problem is to decide whether AB=C. Classically, the best known algorithm achieves this in time $O(n^2)$, whereas the best known classical algorithm for matrix multiplication runs in time $O(n^{2.373})$. Ambainis et al. discovered a quantum algorithm for this problem with runtime $O(n^{7/4})$[[6](#6)]. Subsequently, Buhrman and Špalek improved upon this, obtaining a quantum algorithm for this problem with runtime $O(n^{5/3})$[[19](#19)]. This latter algorithm is based on results regarding quantum walks that were proven in [[85](#85)].

---

### Algorithm: Subset-sum
- **Speedup**: Polynomial
- **Description**: Given a list of integers $x_1,\ldots,x_n$, and a target integer s, the subset-sum problem is to determine whether the sum of any subset of the given integers adds up to s. This problem is NP-complete, and therefore is unlikely to be solvable by classical or quantum algorithms with polynomial worst-case complexity. In the hard instances the given integers are of order $2^n$. In [[178](#178)], a quantum algorithm is given that solves this problem in time $2^{0.241n}$, up to polynomial factors. This quantum algorithm works by applying a variant of Ambainis's quantum walk algorithm for element-distinctness [[7](#7)]to speed up a sophisticated classical algorithm for this problem due to Howgrave-Graham and Joux. The fastest known classical algorithm for subset-sum runs in time $2^{0.291n}$, up to polynomial factors.

---

### Algorithm: Decoding
- **Speedup**: Varies
- **Description**: Classical error correcting codes allow the detection and correction of bit-flips by storing data reduntantly. Maximum-likelihood decoding for arbitrary linear codes is NP-complete in the worst case, but for structured codes or bounded error efficient decoding algorithms are known. Quantum algorithms have been formulated to speed up the decoding of convolutional codes [[238](#238)] and simplex codes [[239](#239)].

---

### Algorithm: Constraint Satisfaction
- **Speedup**: Polynomial
- **Description**: Constraint satisfaction problems, many of which are NP-hard, are ubiquitous in computer science, a canonical example being 3-SAT. If one wishes to satisfy as many constraints as possible rather than all of them, these become combinatorial optimization problems. (See also entry on adiabatic algorithms.) The brute force solution to constraint satisfaction problems can be quadratically sped up using Grover's algorithm. However, most constaint satisfaction problems are solvable by classical algorithms that (although still exponential-time) run more than quadratically faster than brute force checking of all possible solutions. Nevertheless, a polynomial quantum speedup over the fastest known classical algorithm for 3-SAT is given in [[133](#133)], and polynomial quantum speedups for some other constraint satisfaction problems are given in [[134](#134),[298](#298)]. A commonly used classical algorithm for constraint satisfaction is backtracking, and for some problems this algorithm is the fastest known. A general quantum speedup for backtracking algorithms is given in [[264](#264)].

---

### Algorithm: Quantum Cryptanalysis
- **Speedup**: Various
- **Description**: It is well-known that Shor's algorithms for factoring and discrete logarithms [[82](#82),[125](#125)] completely break the RSA and Diffie-Hellman cryptosystems, as well as their elliptic-curve-based variants [[109](#109),[14](#14)]. (A number of "post-quantum" public-key cryptosystems have been proposed to replace these primitives, which are not known to be broken by quantum attacks.) Beyond Shor's algorithm, there is a growing body of work on quantum algorithms specifically designed to attack cryptosystems. These generally fall into three categories. The first is quantum algorithms providing polynomial or sub-exponential time attacks on cryptosystems under standard assumptions. In particular, the algorithm of Childs, Jao, and Soukharev for finding isogenies of elliptic curves breaks certain elliptic curve based cryptosystems in subexponential time that were not already broken by Shor's algorithm [[283](#283)]. The second category is quantum algorithms achieving polynomial improvement over known classical cryptanalytic attacks by speeding up parts of these classical algorithms using Grover search, quantum collision finding, etc. Such attacks on private-key [[284](#284),[285](#285), [288](#288),[315](#315),[316](#316)] and public-key [[262](#262),[287](#287)] primitives, do not preclude the use of the associated cryptosystems but may influence choice of key size. The third category is attacks that make use of quantum superposition queries to block ciphers. These attacks in many cases completely break the cryptographic primitives [[286](#286),[289](#289),[290](#290),[291](#291),[292](#292)]. However, in most practical situations such superposition queries are unlikely to be feasible.

---

## Oracular Algorithms
### Algorithm: Searching
- **Speedup**: Polynomial
- **Description**: We are given an oracle with N allowed inputs. For one input w ("the winner") the corresponding output is 1, and for all other inputs the corresponding output is 0. The task is to find w. On a classical computer this requires $\Omega(N)$ queries. The quantum algorithm of Lov Grover achieves this using $O(\sqrt{N})$ queries [[48](#48)], which is optimal [[216](#216)]. This has algorithm has subsequently been generalized to search in the presence of multiple "winners" [[15](#15)], evaluate the sum of an arbitrary function [[15](#15),[16](#16),[73](#73)], find the global minimum of an arbitrary function [[35](#35),[75](#75),[255](#255)], take advantage of alternative initial states [[100](#100)] or nonuniform probabilistic priors [[123](#123)], work with oracles whose runtime varies between inputs [[138](#138)], approximate definite integrals [[77](#77)], and converge to a fixed-point [[208](#208),[209](#209)]. The generalization of Grover's algorithm known as amplitude estimation [[17](#17)] is now an important primitive in quantum algorithms. Amplitude estimation forms the core of most known quantum algorithms related to collision finding and graph properties. One of the natural applications for Grover search is speeding up the solution to NP-complete problems such as 3-SAT. Doing so is nontrivial, because the best classical algorithm for 3-SAT is not quite a brute force search. Nevertheless, amplitude amplification enables a quadratic quantum speedup over the best classical 3-SAT algorithm, as shown in [[133](#133)]. Quadratic speedups for other constraint satisfaction problems are obtained in [[134](#134)]. For further examples of application of Grover search and amplitude amplification see [[261](#261),[262](#262)]. A problem closely related to, but harder than, Grover search, is spatial search, in which database queries are limited by some graph structure. On sufficiently well-connected graphs, $O(\sqrt{n})$ quantum query complexity is still achievable [[274](#274),[275](#275),[303](#303),[304](#304),[305](#305),[306](#306),[330](#330)].

---

### Algorithm: Abelian Hidden Subgroup
- **Speedup**: Superpolynomial
- **Description**: Let G be a finitely generated Abelian group, and let H be some subgroup of G such that G/H is finite. Let f be a function on G such that for any $g_1,g_2 \in G$, $f(g_1) = f(g_2)$ if and only if $g_1$ and $g_2$ are in the same coset of H. The task is to find H (i.e. find a set of generators for H) by making queries to f. This is solvable on a quantum computer using $O(\log \vert G\vert)$ queries, whereas classically $\Omega(|G|)$ are required. This algorithm was first formulated in full generality by Boneh and Lipton in [[14](#14)]. However, proper attribution of this algorithm is difficult because, as described in chapter 5 of [[76](#76)], it subsumes many historically important quantum algorithms as special cases, including Simon's algorithm [[108](#108)], which was the inspiration for Shor's period finding algorithm, which forms the core of his factoring and discrete-log algorithms. The Abelian hidden subgroup algorithm is also at the core of the Pell's equation, principal ideal, unit group, and class group algorithms. In certain instances, the Abelian hidden subgroup problem can be solved using a single query rather than order $\log(\vert G\vert)$, as shown in [[30](#30)].

---

### Algorithm: Non-Abelian Hidden Subgroup
- **Speedup**: Superpolynomial
- **Description**: Let G be a finitely generated group, and let H be some subgroup of G that has finitely many left cosets. Let f be a function on G such that for any $g_1, g_2$, $f(g_1) = f(g_2)$ if and only if $g_1$ and $g_2$ are in the same left coset of H. The task is to find H (i.e. find a set of generators for H) by making queries to f. This is solvable on a quantum computer using $O(\log(|G|)$ queries, whereas classically $\Omega(|G|)$ are required [[37](#37),[51](#51)]. However, this does not qualify as an efficient quantum algorithm because in general, it may take exponential time to process the quantum states obtained from these queries. Efficient quantum algorithms for the hidden subgroup problem are known for certain specific non-Abelian groups [[81](#81),[55](#55),[72](#72),[53](#53),[9](#9),[22](#22),[56](#56),[71](#71),[57](#57),[43](#43),[44](#44),[28](#28),[126](#126),[207](#207),[273](#273)]. A slightly outdated survey is given in [[69](#69)]. Of particular interest are the symmetric group and the dihedral group. A solution for the symmetric group would solve graph isomorphism. A solution for the dihedral group would solve certain lattice problems [[78](#78)]. Despite much effort, no polynomial-time solution for these groups is known, except in special cases [[312](#312)]. However, Kuperberg [[66](#66)] found a time $2^{O( \sqrt{\log N})})$ algorithm for finding a hidden subgroup of the dihedral group $D_N$. Regev subsequently improved this algorithm so that it uses not only subexponential time but also polynomial space [[79](#79)]. A further improvement in the asymptotic scaling of the required number of qubits is obtained in [[218](#218)]. Quantum query speedups (though not necessarily efficient quantum algorithms in terms of gate count) for somewhat more general problems of testing for isomorphisms of functions under sets of permutations are given in [[311](#311)]

---

### Algorithm: Bernstein-Vazirani
- **Speedup**: Polynomial Directly, Superpolynomial Recursively
- **Description**: We are given an oracle whose input is n bits and whose output is one bit. Given input $x \in \{0,1\}^n$, the output is $x \odot h$, where h is the "hidden" string of n bits, and $\odot$ denotes the bitwise inner product modulo 2. The task is to find h. On a classical computer this requires n queries. As shown by Bernstein and Vazirani [[11](#11)], this can be achieved on a quantum computer using a single query. Furthermore, one can construct recursive versions of this problem, called recursive Fourier sampling, such that quantum computers require exponentially fewer queries than classical computers [[11](#11)]. See [[256](#256),[257](#257)] for related work on the ubiquity of quantum speedups from generic quantum circuits and [[258](#258),[270](#270)] for related work on a quantum query speedup for detecting correlations between the an oracle function and the Fourier transform of another.

---

### Algorithm: Deutsch-Jozsa
- **Speedup**: Exponential over P, none over BPP
- **Description**: We are given an oracle whose input is n bits and whose output is one bit. We are promised that out of the $2^n$ possible inputs, either all of them, none of them, or half of them yield output 1. The task is to distinguish the balanced case (half of all inputs yield output 1) from the constant case (all or none of the inputs yield output 1). It was shown by Deutsch [[32](#32)] that for n=1, this can be solved on a quantum computer using one query, whereas any deterministic classical algorithm requires two. This was historically the first well-defined quantum algorithm achieving a speedup over classical computation. (A related, more recent, pedagogical example is given in [[259](#259)].) A single-query quantum algorithm for arbitrary n was developed by Deutsch and Jozsa in [[33](#33)]. Although probabilistically easy to solve with O(1) queries, the Deutsch-Jozsa problem has exponential worst case deterministic query complexity classically.

---

### Algorithm: Formula Evaluation
- **Speedup**: Polynomial
- **Description**: A Boolean expression is called a formula if each variable is used only once. A formula corresponds to a circuit with no fanout, which consequently has the topology of a tree. By Reichardt's span-program formalism, it is now known [[158](#158)] that the quantum query complexity of any formula of O(1) fanin on N variables is $\Theta(\sqrt{N})$. This result culminates from a long line of work [[27](#27),[8](#8),[80](#80),[159](#159),[160](#160)], which started with the discovery by Farhi et al. [[38](#38)] that NAND trees on $2^n$ variables can be evaluated on quantum computers in time $O(2^{0.5n})$ using a continuous-time quantum walk, whereas classical computers require $\Omega(2^{0.753n})$ queries. In many cases, the quantum formula-evaluation algorithms are efficient not only in query complexity but also in time-complexity. The span-program formalism also yields quantum query complexity lower bounds [[149](#149)]. Although originally discovered from a different point of view, Grover's algorithm can be regarded as a special case of formula evaluation in which every gate is OR. The quantum complexity of evaluating non-boolean formulas has also been studied [[29](#29)], but is not as fully understood. Childs et al. have generalized to the case in which input variables may be repeated (i.e. the first layer of the circuit may include fanout) [[101](#101)]. They obtained a quantum algorithm using $O(\min \{N,\sqrt{S},N^{1/2} G^{1/4} \})$ queries, where N is the number of input variables not including multiplicities, S is the number of inputs counting multiplicities, and G is the number of gates in the formula. References [[164](#164)], [[165](#165)], and [[269](#269)] consider special cases of the NAND tree problem in which the number of NAND gates taking unequal inputs is limited. Some of these cases yield superpolynomial separation between quantum and classical query complexity.

---

### Algorithm: Gradients, Structured Search, and Learning Polynomials
- **Speedup**: Polynomial
- **Description**: Suppose we are given a oracle for computing some smooth function $f:\mathbb{R}^d \to \mathbb{R}$. The inputs and outputs to f are given to the oracle with finitely many bits of precision. The task is to estimate $\nabla f$ at some specified point $\mathbf{x}_0 \in \mathbb{R}^d$. As shown in [[61](#61)], a quantum computer can achieve this using one query, whereas a classical computer needs at least d+1 queries. In [[20](#20)], Bulger suggested potential applications for optimization problems. As shown in appendix D of [[62](#62)], a quantum computer can use the gradient algorithm to find the minimum of a quadratic form in d dimensions using O(d) queries, whereas, as shown in [[94](#94)], a classical computer needs at least $\Omega(d^2)$ queries. Single query quantum algorithms for finding the minima of basins based on Hamming distance were given in [[147](#147),[148](#148),[223](#223)]. The quantum algorithm of [[62](#62)] can also extract all $d^2$ matrix elements of the quadratic form using O(d) queries, and more generally, all $d^n$ nth derivatives of a smooth function of d variables in $O(d^{n-1})$ queries. As shown in [[130](#130),[146](#146)], quadratic forms and multilinear polynomials in d variables over a finite field may be extracted with a factor of d fewer quantum queries than are required classically.

---

### Algorithm: Hidden Shift
- **Speedup**: Superpolynomial
- **Description**: We are given oracle access to some function f on $\mathbb{Z}_N$. We know that f(x) = g(x+s) where g is a known function and s is an unknown shift. The hidden shift problem is to find s. By reduction from Grover's problem it is clear that at least $\sqrt{N}$ queries are necessary to solve hidden shift in general. However, certain special cases of the hidden shift problem are solvable on quantum computers using O(1) queries. In particular, van Dam et al. showed that this can be done if f is a multiplicative character of a finite ring or field [[89](#89)]. The previously discovered shifted Legendre symbol algorithm [[88](#88),[86](#86)] is subsumed as a special case of this, because the Legendre symbol $\left(\frac{x}{p} \right)$ is a multiplicative character of $\mathbb{F}_p$. No classical algorithm running in time O(polylog(N)) is known for these problems. Furthermore, the quantum algorithm for the shifted Legendre symbol problem would break a certain cryptographic pseudorandom generator given the ability to make quantum queries to the generator [[89](#89)]. A quantum speedup for hidden shift problems of difference sets is given in [[312](#312)], and this also subsumes the Legendre symbol problem as a special case. Roetteler has found exponential quantum speedups for finding hidden shifts of certain nonlinear Boolean functions [[105](#105),[130](#130)]. Building on this work, Gavinsky, Roetteler, and Roland have shown [[142](#142)] that the hidden shift problem on random boolean functions $f:\mathbb{Z}_2^n \to \mathbb{Z}_2$ has O(n) average case quantum complexity, whereas the classical query complexity is $\Omega(2^{n/2})$. The results in [[143](#143)], though they are phrased in terms of the hidden subgroup problem for the dihedral group, imply that the quantum query complexity of the hidden shift problem for an injective function on $\mathbb{Z}_N$ is O(log n), whereas the classical query complexity is $\Theta(\sqrt{N})$. However, the best known quantum circuit complexity for injective hidden shift on $\mathbb{Z}_N$ is $O(2^{C \sqrt{\log N}})$, achieved by Kuperberg's sieve algorithm [[66](#66)].

---

### Algorithm: Polynomial interpolation
- **Speedup**: Constant factor
- **Description**: Let $p(x) = a_d x^d + \ldots + a_1 x + a_0$ be a polynomial over the finite field $\mathrm{GF}(q)$. One is given access to an oracle that, given $x \in \mathrm{GF}(q)$, returns $p(x)$. The polynomial interpolation problem is, by making queries to the oracle, to determine the coefficients $a_d,\ldots,a_0$. Classically, $d+1$ queries are necessary and sufficient. Quantumly, $d/2+1/2$ queries are necessary and $d/2+1$ queries are sufficient [[360](#360),[361](#361)].

---

### Algorithm: Pattern matching
- **Speedup**: Superpolynomial
- **Description**: Given strings T of length n and P of length m < n, both from some finite alphabet, the pattern matching problem is to find an occurrence of P as a substring of T or to report that P is not a substring of T. More generally, T and P could be d-dimensional arrays rather than one-dimensional arrays (strings). Then, the pattern matching problem is to return the location of P as a $m \times m \times \ldots \times m$ block within the $n \times n \times \ldots \times n$ array T or report that no such location exists. The $\Omega(\sqrt{N})$ query lower bound for unstructured search [[216](#216)] implies that the worst-case quantum query complexity of this problem is $\Omega ( \sqrt{n} + \sqrt{m} )$. A quantum algorithm achieving this, up to logarithmic factors, was obtained in [[217](#217)]. This quantum algorithm works through the use of Grover's algorithm together with a classical method called deterministic sampling. More recently, Montanaro showed that superpolynomial quantum speedup can be achieved on average case instances of pattern matching, provided that m is greater than logarithmic in n. Specifically, the quantum algorithm given in [[215](#215)] solves average case pattern matching in $\widetilde{O}((n/m)^{d/2} 2^{O(d^{3/2} \sqrt{\log m})})$ time. This quantum algorithm is constructed by generalizing Kuperberg's quantum sieve algorithm [[66](#66)] for dihedral hidden subgroup and hidden shift problems so that it can operate in d dimensions and accomodate small amounts of noise, and then classically reducing the pattern matching problem to this noisy d-dimensional version of hidden shift.

---

### Algorithm: Linear Systems
- **Speedup**: Superpolynomial
- **Description**: We are given oracle access to an $n \times n$ matrix A and some description of a vector b. We wish to find some property of f(A)b for some efficiently computable function f. Suppose A is a Hermitian matrix with O(polylog n) nonzero entries in each row and condition number k. As shown in [[104](#104)], a quantum computer can in $O(k^2 \log n)$ time compute to polynomial precision various expectation values of operators with respect to the vector f(A)b (provided that a quantum state proportional to b is efficiently constructable). For certain functions, such as f(x)=1/x, this procedure can be extended to non-Hermitian and even non-square A. The runtime of this algorithm was subsequently improved to $O(k \log^3 k \log n)$ in [[138](#138)]. Exponentially improved scaling of runtime with precision was obtained in [[263](#263)]. Extensions of this quantum algorithm have been applied to problems of estimating electromagnetic scattering crossections \[[249](#249)\] (see also [[369](#369)] for a different approach), solving linear differential equations [[156](#156),[296](#296)], estimating electrical resistance of networks [[210](#210)], least-squares curve-fitting [[169](#169)], solving Toeplitz systems [[297](#297)], and machine learning [[214](#214),[222](#222),[250](#250),[251](#251),[309](#309)]. Some limitations of the quantum machine learning algorithms based on linear systems are nicely summarized in [[246](#246)]. In [[220](#220)] it was shown that quantum computers can invert well-conditioned $n \times n$ matrices using only $O( \log n )$ qubits, whereas the best classical algorithm uses order $\log^2 n$ bits. Subsequent improvements to this quantum algorithm are given in [[279](#279)].

---

### Algorithm: Ordered Search
- **Speedup**: Constant factor
- **Description**: We are given oracle access to a list of N numbers in order from least to greatest. Given a number x, the task is to find out where in the list it would fit. Classically, the best possible algorithm is binary search which takes $\log_2 N$ queries. Farhi et al. showed that a quantum computer can achieve this using 0.53 $\log_2 N$ queries [[39](#39)]. Currently, the best known deterministic quantum algorithm for this problem uses 0.433 $\log_2 N$ queries [[103](#103)]. A lower bound of $\frac{\ln 2}{\pi} \log_2 N$ quantum queries has been proven for this problem [[219](#219),[24](#24)]. In [[10](#10)], a randomized quantum algorithm is given whose expected query complexity is less than $\frac{1}{3} \log_2 N$.

---

### Algorithm: Graph Properties in the Adjacency Matrix Model
- **Speedup**: Polynomial
- **Description**: Let G be a graph of n vertices. We are given access to an oracle, which given a pair of integers in {1,2,...,n} tells us whether the corresponding vertices are connected by an edge. Building on previous work [[35](#35),[52](#52),[36](#36)], Dürr et al. [[34](#34)] show that the quantum query complexity of finding a minimum spanning tree of weighted graphs, and deciding connectivity for directed and undirected graphs have $\Theta(n^{3/2})$ quantum query complexity, and that finding lowest weight paths has $O(n^{3/2}\log^2 n)$ quantum query complexity. Deciding whether a graph is bipartite, detecting cycles, and deciding whether a given vertex can be reached from another (st-connectivity) can all be achieved using a number of queries and quantum gates that both scale as $\widetilde{O}(n^{3/2})$, and only logarithmically many qubits, as shown in [[317](#317)], building upon [[13](#13),[272](#272),[318](#318)]. A span-program-based quantum algorithm for detecting trees of a given size as minors in $\widetilde{O}(n)$ time is given in [[240](#240)]. A graph property is sparse if there exists a constant c such that every graph with the property has a ratio of edges to vertices at most c. Childs and Kothari have shown that all sparse graph properties have query complexity $\Theta(n^{2/3})$ if they cannot be characterized by a list of forbidden subgraphs and $o(n^{2/3})$ (little-o) if they can [[140](#140)]. The former algorithm is based on Grover search, the latter on the quantum walk formalism of [[141](#141)]. By Mader's theorem, sparse graph properties include all nontrivial minor-closed properties. These include planarity, being a forest, and not containing a path of given length. According to the widely-believed Aanderaa-Karp-Rosenberg conjecture, all of the above problems have $\Omega(n^2)$ classical query complexity. Another interesting computational problem is finding a subgraph H in a given graph G. The simplest case of this finding the triangle, that is, the clique of size three. The fastest known quantum algorithm for this finds a triangle in $O(n^{5/4})$ quantum queries [[319](#319)], improving upon [[276](#276),[175](#175),[171](#171),[70](#70),[152](#152),[21](#21)]. Stronger quantum query complexity upper bounds are known when the graphs are sufficiently sparse [[319](#319),[320](#320)]. Classically, triangle finding requires $\Omega(n^2)$ queries [[21](#21)]. More generally, a quantum computer can find an arbitrary subgraph of k vertices using $O(n^{2-2/k-t})$ queries where $t=(2k-d-3)/(k(d+1)(m+2))$ and d and m are such that H has a vertex of degree d and m+d edges [[153](#153)]. This improves on the previous algorithm of [[70](#70)]. In some cases, this query complexity is beaten by the quantum algorithm of [[140](#140)], which finds H using $\widetilde{O}\left( n^{\frac{3}{2}-\frac{1}{\mathrm{vc}(H)+1}} \right)$ queries, provided G is sparse, where vc(H) is the size of the minimal vertex cover of H. A quantum algorithm for finding constant-sized sub-hypergraphs over 3-uniform hypergraphs in $O(n^{1.883})$ queries is given in [[241](#241)].

---

### Algorithm: Graph Properties in the Adjacency List Model
- **Speedup**: Polynomial
- **Description**: Let G be a graph of N vertices, M edges, and degree d. We are given access to an oracle which, when queried with the label of a vertex and $j \in \{1,2,\ldots,d\}$ outputs the jth neighbor of the vertex or null if the vertex has degree less than d. Suppose we are given the promise that G is either bipartite or is far from bipartite in the sense that a constant fraction of the edges would need to be removed to achieve bipartiteness. Then, as shown in [[144](#144)], the quantum complexity of deciding bipartiteness is $\widetilde{O}(N^{1/3})$. Also in [[144](#144)], it is shown that distinguishing expander graphs from graphs that are far from being expanders has quantum complexity $\widetilde{O}(N^{1/3})$ and $\widetilde{O}(N^{1/4})$, whereas the classical complexity is $\widetilde{\Theta}(\sqrt{N})$. The key quantum algorithmic tool is Ambainis' algorithm for element distinctness. In [[34](#34)], it is shown that finding a minimal spanning tree has quantum query complexity $\Theta(\sqrt{NM})$, deciding graph connectivity has quantum query complexity $\Theta(N)$ in the undirected case, and $\widetilde{\Theta}(\sqrt{NM})$ in the directed case, and computing the lowest weight path from a given source to all other vertices on a weighted graph has quantum query complexity $\widetilde{\Theta}(\sqrt{NM})$. In [[317](#317)] quantum algorithms are given for st-connectivity, deciding bipartiteness, and deciding whether a graph is a forest, which run in $\widetilde{O}(N \sqrt{d})$ time and use only logarithmically many qubits.

---

### Algorithm: Welded Tree
- **Speedup**: Superpolynomial
- **Description**: Some computational problems can be phrased in terms of the query complexity of finding one's way through a maze. That is, there is some graph G to which one is given oracle access. When queried with the label of a given node, the oracle returns a list of the labels of all adjacent nodes. The task is, starting from some source node (i.e. its label), to find the label of a certain marked destination node. As shown by Childs et al. [[26](#26)], quantum computers can exponentially outperform classical computers at this task for at least some graphs. Specifically, consider the graph obtained by joining together two depth-n binary trees by a random "weld" such that all nodes but the two roots have degree three. Starting from one root, a quantum computer can find the other root using poly(n) queries, whereas this is provably impossible using classical queries.

---

### Algorithm: Collision Finding and Element Distinctness
- **Speedup**: Polynomial
- **Description**: Suppose we are given oracle access to a two to one function f on a domain of size N. The collision problem is to find a pair $x,y \in \{1,2,\ldots,N\}$ such that f(x) = f(y). The classical randomized query complexity of this problem is $\Theta(\sqrt{N})$, whereas, as shown by Brassard et al., a quantum computer can achieve this using $O(N^{1/3})$ queries [[18](#18)]. (See also [[315](#315)].) Removing the promise that f is two-to-one yields a problem called element distinctness, which has $\Theta(N)$ classical query complexity. Improving upon [[21](#21)], Ambainis gives a quantum algorithm with query complexity of $O(N^{2/3})$ for element distinctness, which is optimal [[7](#7),[374](#374)]. The problem of deciding whether any k-fold collisions exist is called k-distinctness. Improving upon [[7](#7),[154](#154)], the best quantum query complexity for k-distinctness is $O(n^{3/4 - 1/(4(2^k-1))})$ [[172](#172),[173](#173)]. For k=2,3 this is also the time-complexity, up to logarithmic factors, by [[7](#7)]. For $k>3$ the fastest known quantum algorithm has time complexity $O(n^{(k-1)/k})$[[363](#363)]. Given two functions f and g, on domains of size N and M, respectively a claw is a pair x,y such that f(x) = g(y). In the case that N=M, the algorithm of [[7](#7)] solves claw-finding in $O(N^{2/3})$ queries, improving on the previous $O(N^{3/4} \log N)$ quantum algorithm of [[21](#21)]. Further work gives improved query complexity for various parameter regimes in which $N \neq M$[[364](#364),[365](#365)]. More generally, a related problem to element distinctness, is, given oracle access to a sequence, to estimate the $k^{\mathrm{th}}$ frequency moment $F_k = \sum_j n_j^k$, where $n_j$ is the number of times that j occurs in the sequence. An approximately quadratic speedup for this problem is obtained in [[277](#277)]. See also graph collision.

---

### Algorithm: Graph Collision
- **Speedup**: Polynomial
- **Description**: We are given an undirected graph of n vertices and oracle access to a labelling of the vertices by 1 and 0. The graph collision problem is, by querying this oracle, to decide whether there exist a pair of vertices, connected by an edge, both of which are labelled 1. One can embed Grover's unstructured search problem as an instance of graph collision by choosing the star graph, labelling the center 1, and labelling the remaining vertices by the database entries. Hence, this problem has quantum query complexity $\Omega(\sqrt{n})$ and classical query complexity $\Theta (n)$. In [[70](#70)], Magniez, Nayak, and Szegedy gave a $O(N^{2/3})$-query quantum algorithm for graph collision on general graphs. This remains the best upper bound on quantum query complexity for this problem on general graphs. However, stronger upper bounds have been obtained for several special classes of graphs. Specifically, the quantum query complexity on a graph G is $\widetilde{O}(\sqrt{n} + \sqrt{l})$ where l is the number of non-edges in G [[161](#161)], $O(\sqrt{n} \alpha^{1/6})$ where $\alpha$ is the size of the largest independent set of G [[172](#172)], $O(\sqrt{n} + \sqrt{\alpha^*})$ where $\alpha^*$ is the maximum total degree of any independent set of G [[200](#200)], and $O(\sqrt{n} t^{1/6})$ where t is the treewidth of G [[201](#201)]. Furthermore, the quantum query complexity is $\widetilde{O}(\sqrt{n})$ with high probability for random graphs in which the presence or absence of an edge between each pair of vertices is chosen independently with fixed probability, (i.e. Erdős-Rényi graphs) [[200](#200)]. See [[201](#201)] for a summary of these results as well as new upper bounds for two additional classes of graph that are too complicated to describe here.

---

### Algorithm: Matrix Commutativity
- **Speedup**: Polynomial
- **Description**: We are given oracle access to k matrices, each of which are $n \times n$. Given integers $i,j \in \{1,2,\ldots,n\}$, and $x \in \{1,2,\ldots,k\}$ the oracle returns the ij matrix element of the $x^{\mathrm{th}}$ matrix. The task is to decide whether all of these k matrices commute. As shown by Itakura [[54](#54)], this can be achieved on a quantum computer using $O(k^{4/5}n^{9/5})$ queries, whereas classically this requires $\Omega( k n^2 )$ queries.

---

### Algorithm: Group Commutativity
- **Speedup**: Polynomial
- **Description**: We are given a list of k generators for a group G and access to a blackbox implementing group multiplication. By querying this blackbox we wish to determine whether the group is commutative. The best known classical algorithm is due to Pak and requires O(k) queries. Magniez and Nayak have shown that the quantum query complexity of this task is $\widetilde{\Theta}(k^{2/3})$ [[139](#139)].

---

### Algorithm: Hidden Nonlinear Structures
- **Speedup**: Superpolynomial
- **Description**: Any Abelian group G can be visualized as a lattice. A subgroup H of G is a sublattice, and the cosets of H are all the shifts of that sublattice. The Abelian hidden subgroup problem is normally solved by obtaining superposition over a random coset of the Hidden subgroup, and then taking the Fourier transform so as to sample from the dual lattice. Rather than generalizing to non-Abelian groups (see non-Abelian hidden subgroup), one can instead generalize to the problem of identifying hidden subsets other than lattices. As shown by Childs et al. [[23](#23)] this problem is efficiently solvable on quantum computers for certain subsets defined by polynomials, such as spheres. Decker et al. showed how to efficiently solve some related problems in [[31](#31),[212](#212)].

---

### Algorithm: Center of Radial Function
- **Speedup**: Polynomial
- **Description**: We are given an oracle that evaluates a function f from âd to some arbitrary set S, where f is spherically symmetric. We wish to locate the center of symmetry, up to some precision. (For simplicity, let the precision be fixed.) In [[110](#110)], Liu gives a quantum algorithm, based on a curvelet transform, that solves this problem using a constant number of quantum queries independent of d. This constitutes a polynomial speedup over the classical lower bound, which is $\Omega(d)$ queries. The algorithm works when the function f fluctuates on sufficiently small scales, e.g., when the level sets of f are sufficiently thin spherical shells. The quantum algorithm is shown to work in an idealized continuous model, and nonrigorous arguments suggest that discretization effects should be small.

---

### Algorithm: Group Order and Membership
- **Speedup**: Superpolynomial
- **Description**: Suppose a finite group G is given oracularly in the following way. To every element in G, one assigns a corresponding label. Given an ordered pair of labels of group elements, the oracle returns the label of their product. There are several classically hard problems regarding such groups. One is to find the group's order, given the labels of a set of generators. Another task is, given a bitstring, to decide whether it corresponds to a group element. The constructive version of this membership problem requires, in the yes case, a decomposition of the given element as a product of group generators. Classically, these problems cannot be solved using polylog(|G|) queries even if G is Abelian. For Abelian groups, quantum computers can solve these problems using polylog(|G|) queries by reduction to the Abelian hidden subgroup problem, as shown by Mosca [[74](#74)]. Furthermore, as shown by Watrous [[91](#91)], quantum computers can solve these problems using polylog(|G|) queries for any solvable group. For groups given as matrices over a finite field rather than oracularly, the order finding and constructive membership problems can be solved in polynomial time by using the quantum algorithms for discrete log and factoring [[124](#124)]. See also group isomorphism.

---

### Algorithm: Group Isomorphism
- **Speedup**: Superpolynomial
- **Description**: Let G be a finite group. To every element of G is assigned an arbitrary label (bit string). Given an ordered pair of labels of group elements, the group oracle returns the label of their product. Given access to the group oracles for two groups G and G', and a list of generators for each group, we must decide whether G and G' are isomorphic. For Abelian groups, we can solve this problem using poly(log |G|, log |G'|) queries to the oracle by applying the quantum algorithm of [[127](#127)], which decomposes any Abelian group into a canonical direct product of cyclic groups. The quantum algorithm of [[128](#128)] solves the group isomorphism problem using poly(log |G|, log |G'|) queries for a certain class of non-Abelian groups. Specifically, a group G is in this class if G has a normal Abelian subgroup A and an element y of order coprime to |A| such that G = A, y. Zatloukal has recently given an exponential quantum speedup for some instances of a problem closely related to group isomorphism, namely testing equivalence of group extensions [[202](#202)].

---

### Algorithm: Statistical Difference
- **Speedup**: Polynomial
- **Description**: Suppose we are given two black boxes A and B whose domain is the integers 1 through T and whose range is the integers 1 through N. By choosing uniformly at random among allowed inputs we obtain a probability distribution over the possible outputs. We wish to approximate to constant precision the L1 distance between the probability distributions determined by A and B. Classically the number of necessary queries scales essentially linearly with N. As shown in [[117](#117)], a quantum computer can achieve this using $O(\sqrt{N})$ queries. Approximate uniformity and orthogonality of probability distributions can also be decided on a quantum computer using $O(N^{1/3})$ queries. The main tool is the quantum counting algorithm of [[16](#16)]. A further improved quantum algorithm for this task is obtained in [[265](#265)].

---

### Algorithm: Finite Rings and Ideals
- **Speedup**: Superpolynomial
- **Description**: Suppose we are given black boxes implementing the addition and multiplication operations on a finite ring R, not necessarily commutative, along with a set of generators for R. With respect to addition, R forms a finite Abelian group (R,+). As shown in [[119](#119)], on a quantum computer one can find in poly(log |R|) time a set of additive generators $\{h_1,\ldots,h_m\} \subset R$ such that $(R,+) \simeq \langle h_1 \rangle \times \ldots \times \langle h_M \rangle$ and m is polylogarithmic in |R|. This allows efficient computation of a multiplication tensor for R. As shown in [[118](#118)], one can similarly find an additive generating set for any ideal in R. This allows one to find the intersection of two ideals, find their quotient, prove whether a given ring element belongs to a given ideal, prove whether a given element is a unit and if so find its inverse, find the additive and multiplicative identities, compute the order of an ideal, solve linear equations over rings, decide whether an ideal is maximal, find annihilators, and test the injectivity and surjectivity of ring homomorphisms. As shown in [[120](#120)], one can also use a quantum computer to efficiently decide whether a given polynomial is identically zero on a given finite black box ring. Known classical algorithms for these problems scale as poly(|R|).

---

### Algorithm: Counterfeit Coins
- **Speedup**: Polynomial
- **Description**: Suppose we are given N coins, k of which are counterfeit. The real coins are all of equal weight, and the counterfeit coins are all of some other equal weight. We have a pan balance and can compare the weight of any pair of subsets of the coins. Classically, we need $\Omega(k \log(N/k))$ weighings to identify all of the counterfeit coins. We can introduce an oracle such that given a pair of subsets of the coins of equal cardinality, it outputs one bit indicating balanced or unbalanced. Building on previous work by Terhal and Smolin [[137](#137)], Iwama et al. have shown [[136](#136)] that on a quantum computer, one can identify all of the counterfeit coins using $O(k^{1/4})$ queries. The core techniques behind the quantum speedup are amplitude amplification and the Bernstein-Vazirani algorithm.

---

### Algorithm: Matrix Rank
- **Speedup**: Polynomial
- **Description**: Suppose we are given oracle access to the (integer) entries of an $n \times m$ matrix A. We wish to determine the rank of the matrix. Classically this requires order nm queries. Building on [[149](#149)], Belovs [[150](#150)] gives a quantum algorithm that can use fewer queries given a promise that the rank of the matrix is at least r. Specifically, Belovs' algorithm uses $O(\sqrt{r(n-r+1)}LT)$ queries, where L is the root-mean-square of the reciprocals of the r largest singular values of A and T is a factor that depends on the sparsity of the matrix. For general A, $T = O(\sqrt{nm})$. If A has at most k nonzero entries in any row or column then $T = O(k \log(n+m))$. (To achieve the corresponding query complexity in the k-sparse case, the oracle must take a column index as input, and provide a list of the nonzero matrix elements from that column as output.) As an important special case, one can use these quantum algorithms for the problem of determining whether a square matrix is singular, which is sometimes referred to as the determinant problem. For general A the quantum query complexity of the determinant problem is no lower than the classical query complexity [[151](#151)]. However, [[151](#151)] does not rule out a quantum speedup given a promise on A, such as sparseness or lack of small singular values.

---

### Algorithm: Matrix Multiplication over Semirings
- **Speedup**: Polynomial
- **Description**: A semiring is a set endowed with addition and multiplication operations that obey all the axioms of a ring except the existence additive inverses. Matrix multiplication over various semirings has many applications to graph problems. Matrix multiplication over semirings can be sped up by straightforward Grover improvements upon schoolbook multiplication, yielding a quantum algorithm that multiplies a pair of $n \times n$ matrices in $\widetilde{O}(n^{5/2})$ time. For some semirings this algorithm outperforms the fastest known classical algorithms and for some semirings it does not [[206](#206)]. A case of particular interest is the Boolean semiring, in which OR serves as addition and AND serves as multiplication. No quantum algorithm is known for Boolean semiring matrix multiplication in the general case that beats the best classical algorithm, which has complexity $n^{2.373}$. However, for sparse input our output, quantum speedups are known. Specifically, let A,B be n by n Boolean matrices. Let C=AB, and let l be the number of entries of C that are equal to 1 (i.e. TRUE). Improving upon [[19](#19),[155](#155),[157](#157)], the best known upper bound on quantum query complexity is $\widetilde{O}(n \sqrt{l})$, as shown in [ [161]. If instead the input matrices are sparse, a quantum speedup over the fastest known classical algorithm also has been found in a certain regime [[206](#206)]. For detailed comparison to classical algorithms, see [[155](#155),[206](#206)]. Quantum algorithms have been found to perform matrix multiplication over the (max,min) semiring in $\widetilde{O}(n^{2.473})$ time and over the distance dominance semiring in $\widetilde{O}(n^{2.458})$ time [[206](#206)]. The fastest known classical algorithm for both of these problems has $\widetilde{O}(n^{2.687})$ complexity.

---

### Algorithm: Subset finding
- **Speedup**: Polynomial
- **Description**: We are oracle access to a function $f:D \to R$ where D and R are finite sets. Some property $P \subset (D \times R)^k$ is specified, for example as an explicit list. Our task is to find a size-k subset of D satisfying P, i.e. $((x_1,f(x_1)),\ldots,(x_k,f(x_k)))
 \in P$, or reject if none exists. As usual, we wish to do this with the minimum number of queries to f. Generalizing the result of [[7](#7)], it was shown in [[162](#162)] that this can be achieved using $O(|D|^{k/(k+1)})$ quantum queries. As an noteworthy special case, this algorithm solves the k-subset-sum problem of finding k numbers from a list with some desired sum. A matching lower bound for the quantum query complexity is proven in [[163](#163)].

---

### Algorithm: Search with Wildcards
- **Speedup**: Polynomial
- **Description**: The search with wildcards problem is to identify a hidden n-bit string x by making queries to an oracle f. Given $S \subseteq \{1,2,\ldots,n\}$ and $y \in \{0,1\}^{|S|}$, f returns one if the substring of x specified by S is equal to y, and returns zero otherwise. Classically, this problem has query complexity $\Theta(n)$. As shown in [[167](#167)], the quantum query complexity of this problem is $\Theta(\sqrt{n})$. Interestingly, this quadratic speedup is achieved not through amplitude amplification or quantum walks, but rather through use of the so-called Pretty Good Measurement. The paper [[167](#167)] also gives a quantum speedup for the related problem of combinatorial group testing. This result and subsequent faster quantum algorithms for group testing are discussed in the entry on Junta Testing and Group Testing.

---

### Algorithm: Network flows
- **Speedup**: Polynomial
- **Description**: A network is a directed graph whose edges are labeled with numbers indicating their carrying capacities, and two of whose vertices are designated as the source and the sink. A flow on a network is an assignment of flows to the edges such that no flow exceeds that edge's capacity, and for each vertex other than the source and sink, the total inflow is equal to the total outflow. The network flow problem is, given a network, to find the flow that maximizes the total flow going from source to sink. For a network with n vertices, m edges, and integer capacities of maximum magnitude U, [[168](#168)] gives a quantum algorithm to find the maximal flow in time $O(\min \{n^{7/6} \sqrt{m} \ U^{1/3}, \sqrt{nU}m\} \times \log n)$. The network flow problem is closely related to the problem of finding a maximal matching of a graph, that is, a maximal-size subset of edges that connects each vertex to at most one other vertex. The paper [[168](#168)] gives algorithms for finding maximal matchings that run in time $O(n \sqrt{m+n} \log n)$ if the graph is bipartite, and $O(n^2 ( \sqrt{m/n} + \log n) \log n)$ in the general case. The core of these algorithms is Grover search. The known upper bounds on classical complexity of the network flow and matching problems are complicated to state because different classical algorithms are preferable in different parameter regimes. However, in certain regimes, the above quantum algorithms beat all known classical algorithms. (See [[168](#168)] for details.)

---

### Algorithm: Electrical Resistance
- **Speedup**: Exponential
- **Description**: We are given oracle access to a weighted graph of n vertices and maximum degree d whose edge weights are to be interpreted as electrical resistances. Our task is to compute the resistance between a chosen pair of vertices. Wang gave two quantum algorithms in [[210](#210)] for this task that run in time $\mathrm{poly}( \log n, d, 1/\phi, 1/\epsilon)$, where $\phi$ is the expansion of the graph, and the answer is to be given to within a factor of $1+\epsilon$. Known classical algorithms for this problem are polynomial in n rather than $\log n$. One of Wang's algorithms is based on a novel use of quantum walks. The other is based on the quantum algorithm of [[104](#104)] for solving linear systems of equations. The first quantum query complexity upper bounds for the electrical resistance problem in the adjacency query model are given in [[280](#280)] using approximate span programs.

---

### Algorithm: Machine Learning
- **Speedup**: Varies
- **Description**: Maching learning encompasses a wide variety of computational problems and can be attacked by a wide variety of algorithmic techniques. This entry summarizes quantum algorithmic techniques for improved machine learning. Many of the quantum algorithms here are cross-listed under other headings. In [[214](#214),[222](#222),[250](#250),[251](#251),[309](#309),[338](#338),[339](#339),[359](#359)], quantum algorithms for solving linear systems [[104](#104)] are applied to speed up cluster-finding, principal component analysis, binary classification, and various forms of regression, provided the data satisfies certain conditions. In [[222](#222)], these quantum algorithms for linear systems are applied to speed up the characterization of persistent homology from data sets. A cluster-finding method not based on the linear systems algorithm of [[104](#104)] is given in [[336](#336)]. The papers [[192](#192),[195](#195),[344](#344),[345](#345),[346](#346),[347](#347),[348](#348)] explore the use of adiabatic optimization techniques to speed up the training of classifiers. In [[221](#221)], a method is proposed for training Boltzmann machines by manipulating coherent quantum states with amplitudes proportional to the Boltzmann weights. Polynomial speedups can be obtained by applying Grover search and related techniques such as amplitude amplification to amenable subroutines of state of the art classical machine learning algorithms. See, for example [[358](#358),[340](#340),[341](#341),[342](#342),[343](#343)]. Other quantum machine learning algorithms not falling into one of the above categories include [[337](#337),[349](#349)]. Some limitations of quantum machine learning algorithms are nicely summarized in [[246](#246)]. Many other quantum query algorithms that extract hidden structure of the black-box function could be cast as machine learning algorithms. See for example [[146](#146),[23](#23),[11](#11),[31](#31),[212](#212)]. Query algorithms for learning the majority and "battleship" functions are given in [[224](#224)]. Large quantum advantages for learning from noisy oracles are given in [[236](#236),[237](#237)]. Several recent review articles [[299](#299),[332](#332),[333](#333)] and a book [[331](#331)] are available which summarize the state of the field. There is a related body of work, not strictly within the standard setting of quantum algorithms, regarding quantum learning in the case that the data itself is quantum coherent. See e.g. [[350](#350),[334](#334),[335](#335),[351](#351),[352](#352),[353](#353),[354](#354),[355](#355),[356](#356),[357](#357)].

---

### Algorithm: Junta Testing and Group Testing
- **Speedup**: Polynomial
- **Description**: A function $f:\{0,1\}^n \to \{0,1\}$ is a k-junta if it depends on at most k of its input bits. The k-junta testing problem is to decide whether a given function is a k-junta or is $\epsilon$-far from any k-junta. Althoug it is not obvious, this problem is closely related to group testing. A group testing problem is defined by a function $f:\{1,2,\ldots,n\} \to \{0,1\}$. One is given oracle access to F, which takes as input subsets of $\{1,2,\ldots,n\}$. F(S) = 1 if there exists $x \in S$ such that f(x) = 1 and F(S) = 0 otherwise. In [[266](#266)] a quantum algorithm is given solving the k-junta problem using $\widetilde{O}(\sqrt{k/\epsilon})$ queries and $\widetilde{O}(n \sqrt{k/\epsilon})$ time. This is a quadratic speedup over the classical complexity, and improves upon a previous quantum algorithm for k-junta testing given in [[267](#267)]. A polynomial speedup for a gapped (i.e. approximation) version of group testing is also given in [[266](#266)], improving upon the earlier results of [[167](#167),[268](#268)].

---

## Approximation and Simulation Algorithms
### Algorithm: Quantum Simulation
- **Speedup**: Superpolynomial
- **Description**: It is believed that for any physically realistic Hamiltonian H on n degrees of freedom, the corresponding time evolution operator $e^{-i H t}$ can be implemented using poly(n,t) gates. Unless BPP=BQP, this problem is not solvable in general on a classical computer in polynomial time. Many techniques for quantum simulation have been developed for general classes of Hamiltonians [[25](#25),[95](#95),[92](#92),[5](#5),[12](#12),[170](#170),[205](#205),[211](#211),[244](#244),[245](#245),[278](#278),[293](#293),[294](#294),[295](#295),[372](#372),[382](#382)], chemical dynamics [[63](#63),[68](#68),[227](#227),[310](#310),[375](#375)], condensed matter physics [[1](#1),[99](#99),[145](#145)], relativistic quantum mechanics (the Dirac and Klein-Gordon equations) [[367](#367),[369](#369),[370](#370),[371](#371)], open quantum systems [[376](#376),[377](#377),[378](#378),[379](#379)], and quantum field theory [[107](#107),[166](#166),[228](#228),[229](#229),[230](#230),[368](#368)]. The exponential complexity of classically simulating quantum systems led Feynman to first propose that quantum computers might outperform classical computers on certain tasks [[40](#40)]. Although the problem of finding ground energies of local Hamiltonians is QMA-complete and therefore probably requires exponential time on a quantum computer in the worst case, quantum algorithms have been developed to approximate ground [[102](#102),[231](#231),[232](#232),[233](#233),[234](#234),[235](#235),[308](#308),[321](#321),[322](#322),[380](#380),[381](#381)] and thermal [[132](#132),[121](#121),[281](#281),[282](#282),[307](#307)] states for some classes of Hamiltonians. Efficient quantum algorithms have been also obtained for preparing certain classes of tensor network states [[323](#323),[324](#324),[325](#325),[326](#326),[327](#327),[328](#328)].

---

### Algorithm: Knot Invariants
- **Speedup**: Superpolynomial
- **Description**: As shown by Freedman [[42](#42),[41](#41)], et al., finding a certain additive approximation to the Jones polynomial of the plat closure of a braid at $e^{i 2 \pi/5}$ is a BQP-complete problem. This result was reformulated and extended to $e^{i 2 \pi/k}$ for arbitrary k by Aharonov et al. [[4](#4),[2](#2)]. Wocjan and Yard further generalized this, obtaining a quantum algorithm to estimate the HOMFLY polynomial [[93](#93)], of which the Jones polynomial is a special case. Aharonov et al. subsequently showed that quantum computers can in polynomial time estimate a certain additive approximation to the even more general Tutte polynomial for planar graphs [[3](#3)]. It is not fully understood for what range of parameters the approximation obtained in [[3](#3)] is BQP-hard. (See also partition functions.) Polynomial-time quantum algorithms have also been discovered for additively approximating link invariants arising from quantum doubles of finite groups [[174](#174)]. (This problem is not known to be BQP-hard.) As shown in [[83](#83)], the problem of finding a certain additive approximation to the Jones polynomial of the trace closure of a braid at $e^{i 2 \pi/5}$ is DQC1-complete.

---

### Algorithm: Three-manifold Invariants
- **Speedup**: Superpolynomial
- **Description**: The Turaev-Viro invariant is a function that takes three-dimensional manifolds as input and produces a real number as output. Homeomorphic manifolds yield the same number. Given a three-manifold specified by a Heegaard splitting, a quantum computer can efficiently find a certain additive approximation to its Turaev-Viro invariant, and this approximation is BQP-complete [[129](#129)]. Earlier, in [[114](#114)], a polynomial-time quantum algorithm was given to additively approximate the Witten-Reshitikhin-Turaev (WRT) invariant of a manifold given by a surgery presentation. Squaring the WRT invariant yields the Turaev-Viro invariant. However, it is unknown whether the approximation achieved in [[114](#114)] is BQP-complete. A suggestion of a possible link between quantum computation and three-manifold invariants was also given in [[115](#115)].

---

### Algorithm: Partition Functions
- **Speedup**: Superpolynomial
- **Description**: For a classical system with a finite set of states S the partition function is $Z = \sum_{s \in S} e^{-E(s)/kT}$, where T is the temperature and k is Boltzmann's constant. Essentially every thermodynamic quantity can be calculated by taking an appropriate partial derivative of the partition function. The partition function of the Potts model is a special case of the Tutte polynomial. A quantum algorithm for approximating the Tutte polynomial is given in [[3](#3)]. Some connections between these approaches are discussed in [[67](#67)]. Additional algorithms for estimating partition functions on quantum computers are given in [[112](#112),[113](#113),[45](#45),[47](#47)]. A BQP-completeness result (where the "energies" are allowed to be complex) is also given in [[113](#113)]. A method for approximating partition functions by simulating thermalization processes is given in [[121](#121)]. A quadratic speedup for the approximation of general partition functions is given in [[122](#122)]. A method based on quantum walks, achieving polynomial speedup for evaluating partition functions is given in [[265](#265)].

---

### Algorithm: Adiabatic Algorithms
- **Speedup**: Unknown
- **Description**: In adiabatic quantum computation one starts with an initial Hamiltonian whose ground state is easy to prepare, and slowly varies the Hamiltonian to one whose ground state encodes the solution to some computational problem. By the adiabatic theorem, the system will track the instantaneous ground state provided the variation of the Hamiltonian is sufficiently slow. The runtime of an adiabatic algorithm scales at worst as $1/ \gamma^3$ where $\gamma$ is the minimum eigenvalue gap between the ground state and the first excited state [[185](#185)]. If the Hamiltonian is varied sufficiently smoothly, one can improve this to $\widetilde{O}(1/\gamma^2)$ [[247](#247)]. Adiabatic quantum computation was first proposed by Farhi et al. as a method for solving NP-complete combinatorial optimization problems [[96](#96),[186](#186)]. Adiabatic quantum algorithms for optimization problems typically use "stoquastic" Hamiltonians, which do not suffer from the sign problem. Such algorithms are sometimes referred to as quantum annealing. Adiabatic quantum computation with non-stoquastic Hamiltonians is as powerful as the quantum circuit model [[97](#97)]. Adiabatic algorithms using stoquastic Hamiltonians are probably less powerful [[183](#183)], but may be nevertheless more powerful than classical computation. The asymptotic runtime of adiabatic optimization algorithms is notoriously difficult to analyze, but some progress has been achieved [[179](#179),[180](#180),[181](#181),[182](#182),[187](#187),[188](#188),[189](#189),[190](#190),[191](#191),[226](#226)]. (Also relevant is an earlier literature on quantum annealing, which originally referred to a classical optimization algorithm that works by simulating a quantum process, much as simulated annealing is a classical optimization algorithm that works by simulating a thermal process. See e.g. [[199](#199),[198](#198)].) Adiabatic quantum computers can perform a process somewhat analogous to Grover search in $O(\sqrt{N})$ time [[98](#98)]. Adiabatic quantum algorithms achieving quadratic speedup for a more general class of problems are constructed in [[184](#184)] by adapting techniques from [[85](#85)]. Adiabatic quantum algorithms have been proposed for several specific problems, including PageRank [[176](#176)], machine learning [[192](#192),[195](#195)], and graph problems [[193](#193),[194](#194)]. Some quantum simulation algorithms also use adiabatic state preparation.

---

### Algorithm: Quantum Approximate Optimization
- **Speedup**: Superpolynomial
- **Description**: For many combinatorial optimization problems, finding the exact optimal solution is NP-complete. There are also hardness-of-approximation results proving that finding an approximation with sufficiently small error bound is NP-complete. For certain problems there is a gap between the best error bound achieved by a polynomial-time classical approximation algorithm and the error bound proven to be NP-hard. In this regime there is potential for exponential speedup by quantum computation. In [[242](#242)] a new quantum algorithmic technique called the Quantum Approximate Optimization Algorithm (QAOA) was proposed for finding approximate solutions to combinatorial optimization problems. In [[243](#243)] it was subsequently shown that QAOA solves a combinatorial optimization problem called Max E3LIN2 with a better approximation ratio than any polynomial-time classical algorithm known at the time. However, an efficient classical algorithm achieving an even better approximation ratio (in fact, the approximation ratio saturating the limit set by hardness-of-approximation) was subsequently discovered [[260](#260)]. Presently, the power of QAOA relative to classical computing is an active area of research [[300](#300),[301](#301),[302](#302),[314](#314)].

---

### Algorithm: Semidefinite Programming
- **Speedup**: Superpolynomial
- **Description**: Given a list of m + 1 Hermitian $n \times n$ matrices $C, A_1, A_2, \ldots, A_m$ and m numbers $b_1, \ldots, b_m$, the problem of semidefinite programming is to find the positive semidefinite $n \times n$ matrix X that maximizes tr(CX) subject to the constraints $\mathrm{tr} (A_j X) \leq b_j$ for $j = 1,2,\ldots,m$. Semidefinite programming has many applications in operations research, combinatorial optimization, and quantum information, and it includes linear programming as a special case. Improving upon [[313](#313)], a quantum algorithm is given in [[383](#383)] that approximately solves semidefinite programs to within $\pm \epsilon$ in time $\widetilde{O} (\sqrt{m} \log m \cdot \mathrm{poly}(\log n, r, \epsilon^{-1}))$, where r is the rank of the semidefinite program. This constitutes a quadratic speedup over the fastest classical algorithms when r is small compared to n. The quantum algorithm is based on amplitude amplification and quantum Gibbs sampling [[121](#121),[307](#307)].

---

### Algorithm: Zeta Functions
- **Speedup**: Superpolynomial
- **Description**: Let f(x,y) be a degree-d polynomial over a finite field $\mathbb{F}_p$. Let $N_r$ be the number of projective solutions to f(x,y = 0 over the extension field $\mathbb{F}_{p^r}$. The zeta function for f is defined to be $Z_f(T) = \exp \left( \sum_{r=1}^\infty \frac{N_r}{r} T^r \right)$. Remarkably, $Z_f(T)$ always has the form $Z_f(T) = \frac{Q_f(T)}{(1-pT)(1-T)}$ where $Q_f(T)$ is a polynomial of degree 2g and $g = \frac{1}{2} (d-1)(d-2)$ is called the genus of f. Given $Z_f(T)$ one can easily compute the number of zeros of f over any extension field $\mathbb{F}_{p^r}$. One can similarly define the zeta function when the original field over which f is defined does not have prime order. As shown by Kedlaya [[64](#64)], quantum computers can determine the zeta function of a genus g curve over a finite field $\mathbb{F}_{p^r}$ in $\mathrm{poly}(\log p, r, g)$ time. The fastest known classical algorithms are all exponential in either log(p) or g. In a diffent, but somewhat related contex, van Dam has conjectured that due to a connection between the zeros of Riemann zeta functions and the eigenvalues of certain quantum operators, quantum computers might be able to efficiently approximate the number of solutions to equations over finite fields [[87](#87)].

---

### Algorithm: Weight Enumerators
- **Speedup**: Superpolynomial
- **Description**: Let C be a code on n bits, i.e. a subset of $\mathbb{Z}_2^n$. The weight enumerator of C is $S_C(x,y) = \sum_{c \in C} x^{|c|} y^{n-|c|}$ where |c| denotes the Hamming weight of c. Weight enumerators have many uses in the study of classical codes. If C is a linear code, it can be defined by $C = \{c: Ac = 0\}$ where A is a matrix over $\mathbb{Z}_2$ In this case $S_C(x,y) = \sum_{c:Ac=0} x^{|c|} y^{n-|c|}$. Quadratically signed weight enumerators (QWGTs) are a generalization of this: $S(A,B,x,y) = \sum_{c:Ac=0} (-1)^{c^T B c} x^{|c|} y^{n-|c|}$. Now consider the following special case. Let A be an $n \times n$ matrix over $\mathbb{Z}_2$ such that diag(A)=I. Let lwtr(A) be the lower triangular matrix resulting from setting all entries above the diagonal in A to zero. Let l,k be positive integers. Given the promise that $|S(A,\mathrm{lwtr}(A),k,l)| \geq \frac{1}{2} (k^2+l^2)^{n/2}$ the problem of determining the sign of $S(A,\mathrm{lwtr}(A),k,l)$ is BQP-complete, as shown by Knill and Laflamme in [[65](#65)]. The evaluation of QWGTs is also closely related to the evaluation of Ising and Potts model partition functions [[67](#67),[45](#45),[46](#46)].

---

### Algorithm: Simulated Annealing
- **Speedup**: Polynomial
- **Description**: In simulated annealing, one has a series of Markov chains defined by stochastic matrices $M_1, M_2,\ldots,M_n$. These are slowly varying in the sense that their limiting distributions $\pi_1, \pi_2, \ldots, \pi_n$ satisfy $|\pi_{t+1} -\pi_t| \lt \epsilon$ for some small $\epsilon$. These distributions can often be thought of as thermal distributions at successively lower temperatures. If $\pi_1$ can be easily prepared, then by applying this series of Markov chains one can sample from $\pi_n$. Typically, one wishes for $\pi_n$ to be a distribution over good solutions to some optimization problem. Let $\delta_i$ be the gap between the largest and second largest eigenvalues of $M_i$. Let $\delta = \min_i \delta_i$. The run time of this classical algorithm is proportional to $1/\delta$. Building upon results of Szegedy [[135](#135),[85](#85)], Somma et al. have shown [[84](#84),[177](#177)] that quantum computers can sample from $\pi_n$ with a runtime proportional to $1/\sqrt{\delta}$. Additional methods by which classical Markov chain Monte Carlo algorithms can be sped up using quantum walks are given in [[265](#265)].

---

### Algorithm: String Rewriting
- **Speedup**: Superpolynomial
- **Description**: String rewriting is a fairly general model of computation. String rewriting systems (sometimes called grammars) are specified by a list of rules by which certain substrings are allowed to be replaced by certain other substrings. For example, context free grammars, are equivalent to the pushdown automata. In [[59](#59)], Janzing and Wocjan showed that a certain string rewriting problem is PromiseBQP-complete. Thus quantum computers can solve it in polynomial time, but classical computers probably cannot. Given three strings s,t,t', and a set of string rewriting rules satisfying certain promises, the problem is to find a certain approximation to the difference between the number of ways of obtaining t from s and the number of ways of obtaining t' from s. Similarly, certain problems of approximating the difference in number of paths between pairs of vertices in a graph, and difference in transition probabilities between pairs of states in a random walk are also BQP-complete [[58](#58)].

---

### Algorithm: Matrix Powers
- **Speedup**: Superpolynomial
- **Description**: Quantum computers have an exponential advantage in approximating matrix elements of powers of exponentially large sparse matrices. Suppose we are have an $N \times N$ symmetric matrix A such that there are at most polylog(N) nonzero entries in each row, and given a row index, the set of nonzero entries can be efficiently computed. The task is, for any 1 < i < N, and any m polylogarithmic in N, to approximate $(A^m)_{ii}$ the $i^{\mathrm{th}}$ diagonal matrix element of $A^m$. The approximation is additive to within $b^m \epsilon$ where b is a given upper bound on |A| and $\epsilon$ is of order 1/polylog(N). As shown by Janzing and Wocjan, this problem is PromiseBQP-complete, as is the corresponding problem for off-diagonal matrix elements [[60](#60)]. Thus, quantum computers can solve it in polynomial time, but classical computers probably cannot.

---

# References

References

<a id="1"></a>1  
 Daniel S. Abrams and Seth Lloyd  
 Simulation of many-body Fermi systems on a universal quantum computer.  
 Physical Review Letters, 79(13):2586-2589, 1997.  
 [arXiv:quant-ph/9703054](https://arXiv.org/abs/quant-ph/9703054)

<a id="2"></a>2  
 Dorit Aharonov and Itai Arad  
 The BQP-hardness of approximating the Jones polynomial.  
 New Journal of Physics 13:035019, 2011.  
 [arXiv:quant-ph/0605181](https://arXiv.org/abs/quant-ph/0605181)

<a id="3"></a>3  
 Dorit Aharonov, Itai Arad, Elad Eban, and Zeph Landau  
 Polynomial quantum algorithms for additive approximations of the Potts model and other points of the Tutte plane.  
 [arXiv:quant-ph/0702008](https://arXiv.org/abs/quant-ph/0702008), 2007.

<a id="4"></a>4  
 Dorit Aharonov, Vaughan Jones, and Zeph Landau  
 A polynomial quantum algorithm for approximating the Jones polynomial.  
 In Proceedings of the 38th ACM Symposium on Theory of Computing, 2006.  
 [arXiv:quant-ph/0511096](https://arXiv.org/abs/quant-ph/0511096)

<a id="5"></a>5  
 Dorit Aharonov and Amnon Ta-Shma  
 Adiabatic quantum state generation and statistical zero knowledge.  
 In Proceedings of the 35th ACM Symposium on Theory of Computing, 2003.  
 [arXiv:quant-ph/0301023](https://arXiv.org/abs/quant-ph/0301023).

<a id="6"></a>6  
 A. Ambainis, H. Buhrman, P. Høyer, M. Karpinizki, and P. Kurur  
 Quantum matrix verification.  
 Unpublished Manuscript, 2002.

<a id="7"></a>7  
 Andris Ambainis  
 Quantum walk algorithm for element distinctness.  
 SIAM Journal on Computing, 37:210-239, 2007.  
 [arXiv:quant-ph/0311001](https://arXiv.org/abs/quant-ph/0311001)

<a id="8"></a>8  
 Andris Ambainis, Andrew M. Childs, Ben W.Reichardt, Robert Špalek, and Shengyu Zheng  
 Every AND-OR formula of size N can be evaluated in time n1/2+o(1) on a quantum computer.  
 In Proceedings of the 48th IEEE Symposium on the Foundations of Computer Science, pages 363-372, 2007.  
 [arXiv:quant-ph/0703015](https://arXiv.org/abs/quant-ph/0703015) and [arXiv:0704.3628](https://arXiv.org/abs/0704.3628)

<a id="9"></a>9  
 Dave Bacon, Andrew M. Childs, and Wim van Dam  
 From optimal measurement to efficient quantum algorithms for the hidden subgroup problem over semidirect product groups.  
 In Proceedings of the 46th IEEE Symposium on Foundations of Computer Science, pages 469-478, 2005.  
 [arXiv:quant-ph/0504083](https://arXiv.org/abs/quant-ph/0504083)

<a id="10"></a>10  
 Michael Ben-Or and Avinatan Hassidim  
 Quantum search in an ordered list via adaptive learning.  
 [arXiv:quant-ph/0703231](https://arXiv.org/abs/quant-ph/0703231), 2007.

<a id="11"></a>11  
 Ethan Bernstein and Umesh Vazirani  
 Quantum complexity theory.  
 In Proceedings of the 25th ACM Symposium on the Theory of Computing, pages 11-20, 1993.

<a id="12"></a>12  
 D.W. Berry, G. Ahokas, R. Cleve, and B. C. Sanders  
 Efficient quantum algorithms for simulating sparse Hamiltonians.  
 Communications in Mathematical Physics, 270(2):359-371, 2007.  
 [arXiv:quant-ph/0508139](https://arXiv.org/abs/quant-ph/0508139)

<a id="13"></a>13  
 A. Berzina, A. Dubrovsky, R. Frivalds, L. Lace, and O. Scegulnaja  
 Quantum query complexity for some graph problems.  
 In Proceedings of the 30th Conference on Current Trends in Theory and Practive of Computer Science, pages 140-150, 2004.

<a id="14"></a>14  
 D. Boneh and R. J. Lipton  
 Quantum cryptanalysis of hidden linear functions.  
 In Don Coppersmith, editor, CRYPTO '95, Lecture Notes in Computer Science, pages 424-437. Springer-Verlag, 1995.

<a id="15"></a>15  
 M. Boyer, G. Brassard, P. Høyer, and A. Tapp  
 Tight bounds on quantum searching.  
 Fortschritte der Physik, 46:493-505, 1998.

<a id="16"></a>16  
 G. Brassard, P. Høyer, and A. Tapp  
 Quantum counting.  
 [arXiv:quant-ph/9805082](https://arXiv.org/abs/quant-ph/9805082), 1998.

<a id="17"></a>17  
 Gilles Brassard, Peter Høyer, Michele Mosca, and Alain Tapp  
 Quantum amplitude amplification and estimation.  
 In Samuel J. Lomonaco Jr. and Howard E. Brandt, editors, Quantum Computation and Quantum Information: A Millennium Volume, volume 305 of AMS Contemporary Mathematics Series. American Mathematical Society, 2002.  
 [arXiv:quant-ph/0005055](https://arXiv.org/abs/quant-ph/0005055)

<a id="18"></a>18  
 Gilles Brassard, Peter Høyer, and Alain Tapp  
 Quantum algorithm for the collision problem.  
 ACM SIGACT News, 28:14-19, 1997.  
 [arXiv:quant-ph/9705002](https://arXiv.org/abs/quant-ph/9705002)

<a id="19"></a>19  
 Harry Buhrman and Robert Špalek  
 Quantum verification of matrix products.  
 In Proceedings of the 17th ACM-SIAM Symposium on Discrete Algorithms, pages 880-889, 2006.  
 [arXiv:quant-ph/0409035](https://arXiv.org/abs/quant-ph/0409035)

<a id="20"></a>20  
 David Bulger  
 Quantum basin hopping with gradient-based local optimisation.  
 [arXiv:quant-ph/0507193](http://arXiv.org/abs/quant-ph/0507193), 2005.

<a id="21"></a>21  
 Harry Burhrman, Christoph Dürr, Mark Heiligman, Peter Høyer, Frédéric Magniez, Miklos Santha, and Ronald de Wolf  
 Quantum algorithms for element distinctness.  
 In Proceedings of the 16th IEEE Annual Conference on Computational Complexity, pages 131-137, 2001.  
 [arXiv:quant-ph/0007016](https://arXiv.org/abs/quant-ph/0007016)

<a id="22"></a>22  
 Dong Pyo Chi, Jeong San Kim, and Soojoon Lee  
 Notes on the hidden subgroup problem on some semi-direct product groups.  
 Phys. Lett. A 359(2):114-116, 2006.  
 [arXiv:quant-ph/0604172](https://arXiv.org/abs/quant-ph/0604172)

<a id="23"></a>23  
 A. M. Childs, L. J. Schulman, and U. V. Vazirani  
 Quantum algorithms for hidden nonlinear structures.  
 In Proceedings of the 48th IEEE Symposium on Foundations of Computer Science, pages 395-404, 2007.  
 [arXiv:0705.2784](https://arXiv.org/abs/0705.2784)

<a id="24"></a>24  
 Andrew Childs and Troy Lee  
 Optimal quantum adversary lower bounds for ordered search.  
 Proceedings of ICALP 2008  
 [arXiv:0708.3396](https://arXiv.org/abs/0708.3396)

<a id="25"></a>25  
 Andrew M. Childs  
 Quantum information processing in continuous time.  
 PhD thesis, MIT, 2004.

<a id="26"></a>26  
 Andrew M. Childs, Richard Cleve, Enrico Deotto, Edward Farhi, Sam Gutmann, and Daniel A. Spielman  
 Exponential algorithmic speedup by quantum walk.  
 In Proceedings of the 35th ACM Symposium on Theory of Computing, pages 59-68, 2003.  
 [arXiv:quant-ph/0209131](https://arXiv.org/abs/quant-ph/0209131)

<a id="27"></a>27  
 Andrew M. Childs, Richard Cleve, Stephen P. Jordan, and David Yeung  
 Discrete-query quantum algorithm for NAND trees.  
 Theory of Computing, 5:119-123, 2009.  
 [arXiv:quant-ph/0702160](https://arXiv.org/abs/quant-ph/0702160)

<a id="28"></a>28  
 Andrew M. Childs and Wim van Dam  
 Quantum algorithm for a generalized hidden shift problem.  
 In Proceedings of the 18th ACM-SIAM Symposium on Discrete Algorithms, pages 1225-1232, 2007.  
 [arXiv:quant-ph/0507190](https://arXiv.org/abs/quant-ph/0507190).

<a id="29"></a>29  
 Richard Cleve, Dmitry Gavinsky, and David L. Yeung  
 Quantum algorithms for evaluating MIN-MAX trees.  
 In Theory of Quantum Computation, Communication, and Cryptography, pages 11-15, Springer, 2008. (LNCS Vol. 5106)  
 [arXiv:0710.5794](https://arXiv.org/abs/0710.5794).

<a id="30"></a>30  
 J. Niel de Beaudrap, Richard Cleve, and John Watrous  
 Sharp quantum versus classical query complexity separations.  
 Algorithmica, 34(4):449-461, 2002.  
 [arXiv:quant-ph/0011065v2](https://arXiv.org/abs/quant-ph/0011065v2).

<a id="31"></a>31  
 Thomas Decker, Jan Draisma, and Pawel Wocjan  
 Quantum algorithm for identifying hidden polynomials.  
 Quantum Information and Computation, 9(3):215-230, 2009.  
 [arXiv:0706.1219](https://arXiv.org/abs/0706.1219).

<a id="32"></a>32  
 David Deutsch  
 Quantum theory, the Church-Turing principle, and the universal quantum computer.  
 Proceedings of the Royal Society of London Series A, 400:97-117, 1985.

<a id="33"></a>33  
 David Deutsch and Richard Jozsa  
 Rapid solution of problems by quantum computation.  
 Proceedings of the Royal Society of London Series A, 493:553-558, 1992.

<a id="34"></a>34  
 Christoph Dürr, Mark Heiligman, Peter Høyer, and Mehdi Mhalla  
 Quantum query complexity of some graph problems.  
 SIAM Journal on Computing, 35(6):1310-1328, 2006.  
 [arXiv:quant-ph/0401091](https://arXiv.org/abs/quant-ph/0401091).

<a id="35"></a>35  
 Christoph Dürr and Peter Høyer  
 A quantum algorithm for finding the minimum.  
 [arXiv:quant-ph/9607014](https://arXiv.org/abs/quant-ph/9607014), 1996.

<a id="36"></a>36  
 Christoph Dürr, Mehdi Mhalla, and Yaohui Lei  
 Quantum query complexity of graph connectivity.  
 [arXiv:quant-ph/0303169](https://arXiv.org/abs/quant-ph/0303169), 2003.

<a id="37"></a>37  
 Mark Ettinger, Peter Høyer, and Emanuel Knill  
 The quantum query complexity of the hidden subgroup problem is polynomial.  
 Information Processing Letters, 91(1):43-48, 2004.  
 [arXiv:quant-ph/0401083](https://arXiv.org/abs/quant-ph/0401083).

<a id="38"></a>38  
 Edward Farhi, Jeffrey Goldstone, and Sam Gutmann  
 A quantum algorithm for the Hamiltonian NAND tree.  
 Theory of Computing 4:169-190, 2008.  
 [arXiv:quant-ph/0702144](https://arXiv.org/abs/quant-ph/0702144).

<a id="39"></a>39  
 Edward Farhi, Jeffrey Goldstone, Sam Gutmann, and Michael Sipser  
 Invariant quantum algorithms for insertion into an ordered list.  
 [arXiv:quant-ph/9901059](https://arXiv.org/abs/quant-ph/9901059), 1999.

<a id="40"></a>40  
 Richard P. Feynman  
 Simulating physics with computers.  
 International Journal of Theoretical Physics, 21(6/7):467-488, 1982.

<a id="41"></a>41  
 Michael Freedman, Alexei Kitaev, and Zhenghan Wang  
 Simulation of topological field theories by quantum computers.  
 Communications in Mathematical Physics, 227:587-603, 2002.

<a id="42"></a>42  
 Michael Freedman, Michael Larsen, and Zhenghan Wang  
 A modular functor which is universal for quantum computation.  
 Comm. Math. Phys. 227(3):605-622, 2002.  
 [arXiv:quant-ph/0001108](https://arXiv.org/abs/quant-ph/0001108).

<a id="43"></a>43  
 K. Friedl, G. Ivanyos, F. Magniez, M. Santha, and P. Sen  
 Hidden translation and translating coset in quantum computing.  
 SIAM Journal on Computing Vol. 43, pp. 1-24, 2014.  
 Appeared earlier in Proceedings of the 35th ACM Symposium on Theory of Computing, pages 1-9, 2003.  
 [arXiv:quant-ph/0211091](https://arXiv.org/abs/quant-ph/0211091).

<a id="44"></a>44  
 D. Gavinsky  
 Quantum solution to the hidden subgroup problem for poly-near-Hamiltonian-groups.  
 Quantum Information and Computation, 4:229-235, 2004.

<a id="45"></a>45  
 Joseph Geraci  
 A new connection between quantum circuits, graphs and the Ising partition function  
 Quantum Information Processing, 7(5):227-242, 2008.  
 [arXiv:0801.4833](https://arXiv.org/abs/0801.4833).

<a id="46"></a>46  
 Joseph Geraci and Frank Van Bussel  
 A theorem on the quantum evaluation of weight enumerators for a certain class of cyclic Codes with a note on cyclotomic cosets.  
 [arXiv:cs/0703129](https://arXiv.org/abs/cs/0703129), 2007.

<a id="47"></a>47  
 Joseph Geraci and Daniel A. Lidar  
 On the exact evaluation of certain instances of the Potts partition function by quantum computers.  
 Comm. Math. Phys. Vol. 279, pg. 735, 2008.  
 [arXiv:quant-ph/0703023](https://arXiv.org/abs/quant-ph/0703023).

<a id="48"></a>48  
 Lov K. Grover  
 Quantum mechanics helps in searching for a needle in a haystack.  
 Physical Review Letters, 79(2):325-328, 1997.  
 [arXiv:quant-ph/9605043](https://arXiv.org/abs/quant-ph/9605043).

<a id="49"></a>49  
 Sean Hallgren  
 Polynomial-time quantum algorithms for Pell's equation and the principal ideal problem.  
 In Proceedings of the 34th ACM Symposium on Theory of Computing, 2002.

<a id="50"></a>50  
 Sean Hallgren  
 Fast quantum algorithms for computing the unit group and class group of a number field.  
 In Proceedings of the 37th ACM Symposium on Theory of Computing, 2005.

<a id="51"></a>51  
 Sean Hallgren, Alexander Russell, and Amnon Ta-Shma  
 Normal subgroup reconstruction and quantum computation using group representations.  
 SIAM Journal on Computing, 32(4):916-934, 2003.

<a id="52"></a>52  
 Mark Heiligman  
 Quantum algorithms for lowest weight paths and spanning trees in complete graphs.  
 [arXiv:quant-ph/0303131](http://arXiv.org/abs/quant-ph/0303131), 2003.

<a id="53"></a>53  
 Yoshifumi Inui and François Le Gall  
 Efficient quantum algorithms for the hidden subgroup problem over a class of semi-direct product groups.  
 Quantum Information and Computation, 7(5/6):559-570, 2007.  
 [arXiv:quant-ph/0412033](https://arXiv.org/abs/quant-ph/0412033).

<a id="54"></a>54  
 Yuki Kelly Itakura  
 Quantum algorithm for commutativity testing of a matrix set.  
 Master's thesis, University of Waterloo, 2005.  
 [arXiv:quant-ph/0509206](https://arXiv.org/abs/quant-ph/0509206).

<a id="55"></a>55  
 Gábor Ivanyos, Frédéric Magniez, and Miklos Santha  
 Efficient quantum algorithms for some instances of the non-abelian hidden subgroup problem.  
 In Proceedings of the 13th ACM Symposium on Parallel Algorithms and Architectures, pages 263-270, 2001.  
 [arXiv:quant-ph/0102014](https://arXiv.org/abs/quant-ph/0102014).

<a id="56"></a>56  
 Gábor Ivanyos, Luc Sanselme, and Miklos Santha  
 An efficient quantum algorithm for the hidden subgroup problem in extraspecial groups.  
 In Proceedings of the 24th Symposium on Theoretical Aspects of Computer Science, 2007.  
 [arXiv:quant-ph/0701235](https://arXiv.org/abs/quant-ph/0701235).

<a id="57"></a>57  
 Gábor Ivanyos, Luc Sanselme, and Miklos Santha  
 An efficient quantum algorithm for the hidden subgroup problem in nil-2 groups.  
 In LATIN 2008: Theoretical Informatics, pg. 759-771, Springer (LNCS 4957).  
 [arXiv:0707.1260](https://arXiv.org/abs/0707.1260).

<a id="58"></a>58  
 Dominik Janzing and Pawel Wocjan  
 BQP-complete problems concerning mixing properties of classical random walks on sparse graphs.  
 [arXiv:quant-ph/0610235](https://arXiv.org/abs/quant-ph/0610235), 2006.

<a id="59"></a>59  
 Dominik Janzing and Pawel Wocjan  
 A promiseBQP-complete string rewriting problem.  
 Quantum Information and Computation, 10(3/4):234-257, 2010.  
 [arXiv:0705.1180](https://arXiv.org/abs/0705.1180).

<a id="60"></a>60  
 Dominik Janzing and Pawel Wocjan  
 A simple promiseBQP-complete matrix problem.  
 Theory of Computing, 3:61-79, 2007.  
 [arXiv:quant-ph/0606229](https://arXiv.org/abs/quant-ph/0606229).

<a id="61"></a>61  
 Stephen P. Jordan  
 Fast quantum algorithm for numerical gradient estimation.  
 Physical Review Letters, 95:050501, 2005.  
 [arXiv:quant-ph/0405146](https://arXiv.org/abs/quant-ph/0405146).

<a id="62"></a>62  
 Stephen P. Jordan  
 Quantum Computation Beyond the Circuit Model.  
 PhD thesis, Massachusetts Institute of Technology, 2008.  
 [arXiv:0809.2307](https://arXiv.org/abs/0809.2307).

<a id="63"></a>63  
 Ivan Kassal, Stephen P. Jordan, Peter J. Love, Masoud Mohseni, and Alán Aspuru-Guzik  
 Quantum algorithms for the simulation of chemical dynamics.  
 Proc. Natl. Acad. Sci. Vol. 105, pg. 18681, 2008.  
 [arXiv:0801.2986](https://arXiv.org/abs/0801.2986).

<a id="64"></a>64  
 Kiran S. Kedlaya  
 Quantum computation of zeta functions of curves.  
 Computational Complexity, 15:1-19, 2006.  
 [arXiv:math/0411623](https://arXiv.org/abs/math/0411623).

<a id="65"></a>65  
 E. Knill and R. Laflamme  
 Quantum computation and quadratically signed weight enumerators.  
 Information Processing Letters, 79(4):173-179, 2001.  
 [arXiv:quant-ph/9909094](https://arXiv.org/abs/quant-ph/9909094).

<a id="66"></a>66  
 Greg Kuperberg  
 A subexponential-time quantum algorithm for the dihedral hidden subgroup problem.  
 SIAM Journal on Computing, 35(1):170-188, 2005.  
 [arXiv:quant-ph/0302112](https://arXiv.org/abs/quant-ph/0302112).

<a id="67"></a>67  
 Daniel A. Lidar  
 On the quantum computational complexity of the Ising spin glass partition function and of knot invariants.  
 New Journal of Physics Vol. 6, pg. 167, 2004.  
 [arXiv:quant-ph/0309064](https://arXiv.org/abs/quant-ph/0309064).

<a id="68"></a>68  
 Daniel A. Lidar and Haobin Wang  
 Calculating the thermal rate constant with exponential speedup on a quantum computer.  
 Physical Review E, 59(2):2429-2438, 1999.  
 [arXiv:quant-ph/9807009](https://arXiv.org/abs/quant-ph/9807009).

<a id="69"></a>69  
 Chris Lomont  
 The hidden subgroup problem - review and open problems.  
 [arXiv:quant-ph/0411037](https://arXiv.org/abs/quant-ph/0411037), 2004.

<a id="70"></a>70  
 Frédéric Magniez, Miklos Santha, and Mario Szegedy  
 Quantum algorithms for the triangle problem.  
 SIAM Journal on Computing, 37(2):413-424, 2007.  
 [arXiv:quant-ph/0310134](https://arXiv.org/abs/quant-ph/0310134).

<a id="71"></a>71  
 Carlos Magno, M. Cosme, and Renato Portugal  
 Quantum algorithm for the hidden subgroup problem on a class of semidirect product groups.  
 [arXiv:quant-ph/0703223](https://arXiv.org/abs/quant-ph/0703223), 2007.

<a id="72"></a>72  
 Cristopher Moore, Daniel Rockmore, Alexander Russell, and Leonard Schulman  
 The power of basis selection in Fourier sampling: the hidden subgroup problem in affine groups.  
 In Proceedings of the 15th ACM-SIAM Symposium on Discrete Algorithms, pages 1113-1122, 2004.  
 [arXiv:quant-ph/0211124](https://arXiv.org/abs/quant-ph/0211124).

<a id="73"></a>73  
 M. Mosca  
 Quantum searching, counting, and amplitude amplification by eigenvector analysis.  
 In R. Freivalds, editor, Proceedings of International Workshop on Randomized Algorithms, pages 90-100, 1998.

<a id="74"></a>74  
 Michele Mosca  
 Quantum Computer Algorithms.  
 PhD thesis, University of Oxford, 1999.

<a id="75"></a>75  
 Ashwin Nayak and Felix Wu  
 The quantum query complexity of approximating the median and related statistics.  
 In Proceedings of 31st ACM Symposium on the Theory of Computing, 1999.  
 [arXiv:quant-ph/9804066](https://arXiv.org/abs/quant-ph/9804066).

<a id="76"></a>76  
 Michael A. Nielsen and Isaac L. Chuang.  
 Quantum Computation and Quantum Information.  
 Cambridge University Press, Cambridge, UK, 2000.

<a id="77"></a>77  
 Erich Novak  
 Quantum complexity of integration.  
 Journal of Complexity, 17:2-16, 2001.  
 [arXiv:quant-ph/0008124](https://arXiv.org/abs/quant-ph/0008124).

<a id="78"></a>78  
 Oded Regev  
 Quantum computation and lattice problems.  
 In Proceedings of the 43rd Symposium on Foundations of Computer Science, 2002.  
 [arXiv:cs/0304005](https://arXiv.org/abs/cs/0304005).

<a id="79"></a>79  
 Oded Regev  
 A subexponential time algorithm for the dihedral hidden subgroup problem with polynomial space.  
 [arXiv:quant-ph/0406151](https://arXiv.org/abs/quant-ph/0406151), 2004.

<a id="80"></a>80  
 Ben Reichardt and Robert Špalek  
 Span-program-based quantum algorithm for evaluating formulas.  
 Proceedings of STOC 2008  
 [arXiv:0710.2630](https://arXiv.org/abs/0710.2630).

<a id="81"></a>81  
 Martin Roetteler and Thomas Beth  
 Polynomial-time solution to the hidden subgroup problem for a class of non-abelian groups.  
 [arXiv:quant-ph/9812070](https://arXiv.org/abs/quant-ph/9812070), 1998.

<a id="82"></a>82  
 Peter W. Shor  
 Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer.  
  SIAM Journal on Computing, 26(5):1484-1509, 1997.  
  [arXiv:quant-ph/9508027](https://arXiv.org/abs/quant-ph/9508027).

<a id="83"></a>83  
 Peter W. Shor and Stephen P. Jordan  
 Estimating Jones polynomials is a complete problem for one clean qubit.  
 Quantum Information and Computation, 8(8/9):681-714, 2008.  
 [arXiv:0707.2831](https://arXiv.org/abs/0707.2831).

<a id="84"></a>84  
 R. D. Somma, S. Boixo, and H. Barnum  
 Quantum simulated annealing.  
 [arXiv:0712.1008](https://arXiv.org/abs/0712.1008), 2007.

<a id="85"></a>85  
 M. Szegedy  
 Quantum speed-up of Markov chain based algorithms.  
 In Proceedings of the 45th IEEE Symposium on Foundations of Computer Science, pg. 32, 2004.

<a id="86"></a>86  
 Wim van Dam  
 Quantum algorithms for weighing matrices and quadratic residues.  
 Algorithmica, 34(4):413-428, 2002.  
 [arXiv:quant-ph/0008059](https://arXiv.org/abs/quant-ph/0008059).

<a id="87"></a>87  
 Wim van Dam  
 Quantum computing and zeros of zeta functions.  
 [arXiv:quant-ph/0405081](https://arXiv.org/abs/quant-ph/0405081), 2004.

<a id="88"></a>88  
 Wim van Dam and Sean Hallgren  
 Efficient quantum algorithms for shifted quadratic character problems.  
 [arXiv:quant-ph/0011067](https://arXiv.org/abs/quant-ph/0011067), 2000.

<a id="89"></a>89  
 Wim van Dam, Sean Hallgren, and Lawrence Ip  
 Quantum algorithms for some hidden shift problems.  
 SIAM Journal on Computing, 36(3):763-778, 2006.  
 [arXiv:quant-h/0211140](https://arXiv.org/abs/quant-h/0211140).

<a id="90"></a>90  
 Wim van Dam and Gadiel Seroussi  
 Efficient quantum algorithms for estimating Gauss sums.  
 [arXiv:quant-ph/0207131](https://arXiv.org/abs/quant-ph/0207131), 2002.

<a id="91"></a>91  
 John Watrous  
 Quantum algorithms for solvable groups.  
 In Proceedings of the 33rd ACM Symposium on Theory of Computing, pages 60-67, 2001.  
 [arXiv:quant-ph/0011023](https://arXiv.org/abs/quant-ph/0011023).

<a id="92"></a>92  
 Stephen Wiesner  
 Simulations of many-body quantum systems by a quantum computer.  
 [arXiv:quant-ph/9603028](https://arXiv.org/abs/quant-ph/9603028), 1996.

<a id="93"></a>93  
 Pawel Wocjan and Jon Yard  
 The Jones polynomial: quantum algorithms and applications in quantum complexity theory.  
 Quantum Information and Computation 8(1/2):147-180, 2008.  
 [arXiv:quant-ph/0603069](https://arXiv.org/abs/quant-ph/0603069).

<a id="94"></a>94  
 Andrew Yao  
 On computing the minima of quadratic forms.  
 In Proceedings of the 7th ACM Symposium on Theory of Computing, pages 23-26, 1975.

<a id="95"></a>95  
 Christof Zalka  
 Efficient simulation of quantum systems by quantum computers.  
 Proceedings of the Royal Society of London Series A, 454:313, 1996.  
 [arXiv:quant-ph/9603026](https://arXiv.org/abs/quant-ph/9603026).

<a id="96"></a>96  
 Edward Farhi, Jeffrey Goldstone, Sam Gutmann, and Michael Sipser  
 Quantum computation by adiabatic evolution.  
 [arXiv:quant-ph/0001106](https://arXiv.org/abs/quant-ph/0001106), 2000.

<a id="97"></a>97  
 Dorit Aharonov, Wim van Dam, Julia Kempe, Zeph Landau, Seth Lloyd, and Oded Regev  
 Adiabatic Quantum Computation is Equivalent to Standard Quantum Computation.  
 SIAM Journal on Computing, 37(1):166-194, 2007.  
 [arXiv:quant-ph/0405098](https://arXiv.org/abs/quant-ph/0405098)

<a id="98"></a>98  
 Jérémie Roland and Nicolas J. Cerf  
 Quantum search by local adiabatic evolution.  
 Physical Review A, 65(4):042308, 2002.  
 [arXiv:quant-ph/0107015](https://arXiv.org/abs/quant-ph/0107015)

<a id="99"></a>99  
 L.-A. Wu, M.S. Byrd, and D. A. Lidar  
 Polynomial-Time Simulation of Pairing Models on a Quantum Computer.  
 Physical Review Letters, 89(6):057904, 2002.  
 [arXiv:quant-ph/0108110](https://arXiv.org/abs/quant-ph/0108110)

<a id="100"></a>100  
 Eli Biham, Ofer Biham, David Biron, Markus Grassl, and Daniel Lidar  
 Grover's quantum search algorithm for an arbitrary initial amplitude distribution.  
 Physical Review A, 60(4):2742, 1999.  
 [arXiv:quant-ph/9807027](https://arXiv.org/abs/quant-ph/9807027) and [arXiv:quant-ph/0010077](https://arXiv.org/abs/quant-ph/0010077)

<a id="101"></a>101  
 Andrew Childs, Shelby Kimmel, and Robin Kothari  
 The quantum query complexity of read-many formulas  
 In Proceedings of ESA 2012, pg. 337-348, Springer. (LNCS 7501)  
 [arXiv:1112.0548](https://arXiv.org/abs/1112.0548), 2011.

<a id="102"></a>102  
 Alán Aspuru-Guzik, Anthony D. Dutoi, Peter J. Love, and Martin Head-Gordon  
 Simulated quantum computation of molecular energies.  
 Science, 309(5741):1704-1707, 2005.  
 [arXiv:quant-ph/0604193](https://arXiv.org/abs/quant-ph/0604193)

<a id="103"></a>103  
 A. M. Childs, A. J. Landahl, and P. A. Parrilo  
 Quantum algorithms for the ordered search problem via semidefinite programming.  
 Physical Review A, 75 032335, 2007.  
 [arXiv:quant-ph/0608161](https://arXiv.org/abs/quant-ph/0608161)

<a id="104"></a>104  
 Aram W. Harrow, Avinatan Hassidim, and Seth Lloyd  
 Quantum algorithm for solving linear systems of equations.  
 Physical Review Letters 15(103):150502, 2009.  
 [arXiv:0811.3171](https://arXiv.org/abs/0811.3171).

<a id="105"></a>105  
 Martin Roetteler  
 Quantum algorithms for highly non-linear Boolean functions.  
 Proceedings of SODA 2010  
 [arXiv:0811.3208](https://arXiv.org/abs/0811.3208).

<a id="106"></a>106  
 Stephen P. Jordan  
 Fast quantum algorithms for approximating the irreducible representations of groups.  
 [arXiv:0811.0562](https://arXiv.org/abs/0811.0562), 2008.

<a id="107"></a>107  
 Tim Byrnes and Yoshihisa Yamamoto  
 Simulating lattice gauge theories on a quantum computer.  
 Physical Review A, 73, 022328, 2006.  
 [arXiv:quant-ph/0510027](https://arXiv.org/abs/quant-ph/0510027).

<a id="108"></a>108  
 D. Simon  
 On the Power of Quantum Computation.  
 In Proceedings of the 35th Symposium on Foundations of Computer  
 Science, pg. 116-123, 1994.

<a id="109"></a>109  
 John Proos and Christof Zalka  
 Shor's discrete logarithm quantum algorithm for elliptic curves.  
 Quantum Information and Computation, Vol. 3, No. 4, pg.317-344, 2003.  
 [arXiv:quant-ph/0301141](https://arXiv.org/abs/quant-ph/0301141).

<a id="110"></a>110  
 Yi-Kai Liu  
 Quantum algorithms using the curvelet transform.  
 Proceedings of STOC 2009, pg. 391-400.  
 [arXiv:0810.4968](https://arXiv.org/abs/0810.4968).

<a id="111"></a>111  
 Wim van Dam and Igor Shparlinski  
 Classical and quantum algorithms for exponential congruences.  
 Proceedings of TQC 2008, pg. 1-10.  
 [arXiv:0804.1109](https://arXiv.org/abs/0804.1109).

<a id="112"></a>112  
 Itai Arad and Zeph Landau  
 Quantum computation and the evaluation of tensor networks.  
 SIAM Journal on Computing, 39(7):3089-3121, 2010.  
 [arXiv:0805.0040](https://arXiv.org/abs/0805.0040).

<a id="113"></a>113  
 M. Van den Nest, W. Dür, R. Raussendorf, and H. J. Briegel  
 Quantum algorithms for spin models and simulable gate sets for quantum computation.  
 Physical Review A, 80:052334, 2009.  
 [arXiv:0805.1214](https://arXiv.org/abs/0805.1214).

<a id="114"></a>114  
 Silvano Garnerone, Annalisa Marzuoli, and Mario Rasetti  
 Efficient quantum processing of 3-manifold topological invariants.  
 Advances in Theoretical and Mathematical Physics, 13(6):1601-1652, 2009.  
 [arXiv:quant-ph/0703037](https://arXiv.org/abs/quant-ph/0703037).

<a id="115"></a>115  
 Louis H. Kauffman and Samuel J. Lomonaco Jr.  
 q-deformed spin networks, knot polynomials and anyonic topological quantum computation.  
 Journal of Knot Theory, Vol. 16, No. 3, pg. 267-332, 2007.  
 [arXiv:quant-ph/0606114](https://arXiv.org/abs/quant-ph/0606114).

<a id="116"></a>116  
 Arthur Schmidt and Ulrich Vollmer  
 Polynomial time quantum algorithm for the computation of the unit group of a number field.  
 In Proceedings of the 37th Symposium on the Theory of Computing, pg. 475-480, 2005.

<a id="117"></a>117  
 Sergey Bravyi, Aram Harrow, and Avinatan Hassidim  
 Quantum algorithms for testing properties of distributions.  
 IEEE Transactions on Information Theory 57(6):3971-3981, 2011.  
 [arXiv:0907.3920](https://arXiv.org/abs/0907.3920).

<a id="118"></a>118  
 Pawel M. Wocjan, Stephen P. Jordan, Hamed Ahmadi, and Joseph P. Brennan  
 Efficient quantum processing of ideals in finite rings.  
 [arXiv:0908.0022](https://arXiv.org/abs/0908.0022), 2009.

<a id="119"></a>119  
 V. Arvind, Bireswar Das, and Partha Mukhopadhyay  
 The complexity of black-box ring problems.  
 In Proceedings of COCCOON 2006, pg 126-145.

<a id="120"></a>120  
 V. Arvind and Partha Mukhopadhyay  
 Quantum query complexity of multilinear identity testing.  
 In Proceedings of STACS 2009, pg. 87-98.

<a id="121"></a>121  
 David Poulin and Pawel Wocjan  
 Sampling from the thermal quantum Gibbs state and evaluating partition functions with a quantum computer.  
 Physical Review Letters 103:220502, 2009.  
 [arXiv:0905.2199](https://arXiv.org/abs/0905.2199)

<a id="122"></a>122  
 Pawel Wocjan, Chen-Fu Chiang, Anura Abeyesinghe, and Daniel Nagaj  
 Quantum speed-up for approximating partition functions.  
 Physical Review A 80:022340, 2009.  
 [arXiv:0811.0596](https://arXiv.org/abs/0811.0596)

<a id="123"></a>123  
 Ashley Montanaro  
 Quantum search with advice.  
 In Proceedings of the 5th conference on Theory of quantum computation, communication, and cryptography (TQC 2010)  
 [arXiv:0908.3066](https://arXiv.org/abs/0908.3066)

<a id="124"></a>124  
 Laszlo Babai, Robert Beals, and Akos Seress  
 Polynomial-time theory of matrix groups.  
 In Proceedings of STOC 2009, pg. 55-64.

<a id="125"></a>125  
 Peter Shor  
 Algorithms for Quantum Computation: Discrete Logarithms and Factoring.  
 In Proceedings of FOCS 1994, pg. 124-134.

<a id="126"></a>126  
 Aaron Denney, Cristopher Moore, and Alex Russell  
 Finding conjugate stabilizer subgroups in PSL(2;q) and related groups.  
 Quantum Information and Computation 10(3):282-291, 2010.  
 [arXiv:0809.2445](https://arXiv.org/abs/0809.2445).

<a id="127"></a>127  
 Kevin K. H. Cheung and Michele Mosca  
 Decomposing finite Abelian groups.  
 Quantum Information and Computation 1(2):26-32, 2001.  
 [arXiv:cs/0101004](https://arXiv.org/abs/cs/0101004).

<a id="128"></a>128  
 François Le Gall  
 An efficient quantum algorithm for some instances of the group isomorphism problem.  
 In Proceedings of STACS 2010.  
 [arXiv:1001.0608](https://arXiv.org/abs/1001.0608).

<a id="129"></a>129  
 Gorjan Alagic, Stephen Jordan, Robert Koenig, and Ben Reichardt  
 Approximating Turaev-Viro 3-manifold invariants is universal for quantum computation.  
 Physical Review A 82, 040302(R), 2010.  
 [arXiv:1003.0923](https://arXiv.org/abs/1003.0923)

<a id="130"></a>130  
 Martin Rötteler  
 Quantum algorithms to solve the hidden shift problem for quadratics and for functions of large Gowers norm.  
 In Proceedings of MFCS 2009, pg 663-674.  
 [arXiv:0911.4724](https://arXiv.org/abs/0911.4724).

<a id="131"></a>131  
 Arthur Schmidt  
 Quantum Algorithms for many-to-one Functions to Solve the Regulator and the Principal Ideal Problem.  
 [arXiv:0912.4807](https://arXiv.org/abs/0912.4807), 2009.

<a id="132"></a>132  
 K. Temme, T.J. Osborne, K.G. Vollbrecht, D. Poulin, and F. Verstraete  
 Quantum Metropolis Sampling.  
 Nature, Vol. 471, pg. 87-90, 2011.  
 [arXiv:0911.3635](https://arXiv.org/abs/0911.3635).

<a id="133"></a>133  
 Andris Ambainis  
 Quantum Search Algorithms.  
 SIGACT News, 35 (2):22-35, 2004.  
 [arXiv:quant-ph/0504012](https://arXiv.org/abs/quant-ph/0504012)

<a id="134"></a>134  
 Nicolas J. Cerf, Lov K. Grover, and Colin P. Williams  
 Nested quantum search and NP-hard problems.  
 Applicable Algebra in Engineering, Communication and Computing, 10 (4-5):311-338, 2000.

<a id="135"></a>135  
 Mario Szegedy  
 Spectra of Quantized Walks and a $\sqrt{\delta \epsilon}$ rule.  
 [arXiv:quant-ph/0401053](https://arXiv.org/abs/quant-ph/0401053), 2004.

<a id="136"></a>136  
 Kazuo Iwama, Harumichi Nishimura, Rudy Raymond, and Junichi Teruyama  
 Quantum Counterfeit Coin Problems.  
 In Proceedings of 21st International Symposium on Algorithms and Computation (ISAAC2010), LNCS 6506, pp.73-84, 2010.  
 [arXiv:1009.0416](https://arXiv.org/abs/1009.0416)

<a id="137"></a>137  
 Barbara Terhal and John Smolin  
 Single quantum querying of a database.  
 Physical Review A 58:1822, 1998.  
 [arXiv:quant-ph/9705041](https://arXiv.org/abs/quant-ph/9705041)

<a id="138"></a>138  
 Andris Ambainis  
 Variable time amplitude amplification and a faster quantum algorithm for solving systems of linear equations.  
 [arXiv:1010.4458](https://arXiv.org/abs/1010.4458), 2010.

<a id="139"></a>139  
 Frédéric Magniez and Ashwin Nayak  
 Quantum complexity of testing group commutativity.  
 In Proceedings of 32nd International Colloquium on Automata, Languages and Programming. LNCS 3580, pg. 1312-1324, 2005.  
 [arXiv:quant-ph/0506265](https://arXiv.org/abs/quant-ph/0506265)

<a id="140"></a>140  
 Andrew Childs and Robin Kothari  
 Quantum query complexity of minor-closed graph properties.  
 In Proceedings of the 28th Symposium on Theoretical Aspects of Computer Science (STACS 2011), pg. 661-672  
 [arXiv:1011.1443](https://arXiv.org/abs/1011.1443)

<a id="141"></a>141  
 Frédéric Magniez, Ashwin Nayak, Jérémie Roland, and Miklos Santha  
 Search via quantum walk.  
 In Proceedings STOC 2007, pg. 575-584.  
 [arXiv:quant-ph/0608026](https://arXiv.org/abs/quant-ph/0608026)

<a id="142"></a>142  
 Dmitry Gavinsky, Martin Roetteler, and Jérémy Roland  
 Quantum algorithm for the Boolean hidden shift problem.  
 In Proceedings of the 17th annual international conference on Computing and combinatorics (COCOON '11), 2011.  
 [arXiv:1103.3017](https://arXiv.org/abs/1103.3017)

<a id="143"></a>143  
 Mark Ettinger and Peter Høyer  
 On quantum algorithms for noncommutative hidden subgroups.  
 Advances in Applied Mathematics, Vol. 25, No. 3, pg. 239-251, 2000.  
 [arXiv:quant-ph/9807029](https://arXiv.org/abs/quant-ph/9807029)

<a id="144"></a>144  
 Andris Ambainis, Andrew Childs, and Yi-Kai Liu  
 Quantum property testing for bounded-degree graphs.  
 In Proceedings of RANDOM '11: Lecture Notes in Computer Science 6845, pp. 365-376, 2011.  
 [arXiv:1012.3174](https://arXiv.org/abs/1012.3174)

<a id="145"></a>145  
 G. Ortiz, J.E. Gubernatis, E. Knill, and R. Laflamme  
 Quantum algorithms for Fermionic simulations.  
 Physical Review A 64: 022319, 2001.  
 [arXiv:cond-mat/0012334](https://arXiv.org/abs/cond-mat/0012334)

<a id="146"></a>146  
 Ashley Montanaro  
 The quantum query complexity of learning multilinear polynomials.  
 Information Processing Letters, 112(11):438-442, 2012.  
 [arXiv:1105.3310](https://arXiv.org/abs/1105.3310).

<a id="147"></a>147  
 Tad Hogg  
 Highly structured searches with quantum computers.  
 Physical Review Letters 80: 2473, 1998.

<a id="148"></a>148  
 Markus Hunziker and David A. Meyer  
 Quantum algorithms for highly structured search problems.  
 Quantum Information Processing, Vol. 1, No. 3, pg. 321-341, 2002.

<a id="149"></a>149  
 Ben Reichardt  
 Span programs and quantum query complexity: The general adversary bound is nearly tight for every Boolean function.  
 In Proceedings of the 50th IEEE Symposium on Foundations of Computer Science (FOCS '09), pg. 544-551, 2009.  
 [arXiv:0904.2759](https://arXiv.org/abs/0904.2759)

<a id="150"></a>150  
 Aleksandrs Belovs  
 Span-program-based quantum algorithm for the rank problem.  
 [arXiv:1103.0842](https://arXiv.org/abs/1103.0842), 2011.

<a id="151"></a>151  
 Sebastian Dörn and Thomas Thierauf  
 The quantum query complexity of the determinant.  
 Information Processing Letters Vol. 109, No. 6, pg. 305-328, 2009.

<a id="152"></a>152  
 Aleksandrs Belovs  
 Span programs for functions with constant-sized 1-certificates.  
 In Proceedings of STOC 2012, pg. 77-84.  
 [arXiv:1105.4024](https://arXiv.org/abs/1105.4024).

<a id="153"></a>153  
 Troy Lee, Frédéric Magniez, and Mikos Santha  
 A learning graph based quantum query algorithm for finding constant-size subgraphs.  
 Chicago Journal of Theoretical Computer Science, Vol. 2012, Article 10, 2012.  
 [arXiv:1109.5135](https://arXiv.org/abs/1109.5135).

<a id="154"></a>154  
 Aleksandrs Belovs and Troy Lee  
 Quantum algorithm for k-distinctness with prior knowledge on the input.  
 [arXiv:1108.3022](https://arXiv.org/abs/1108.3022), 2011.

<a id="155"></a>155  
 François Le Gall  
 Improved output-sensitive quantum algorithms for Boolean matrix multiplication.  
 In Proceedings of the 23rd Annual ACM-SIAM Symposium on Discrete Algorithms (SODA '12), 2012.

<a id="156"></a>156  
 Dominic Berry  
 Quantum algorithms for solving linear differential equations.  
 [arXiv:1010.2745](https://arXiv.org/abs/1010.2745), 2010.

<a id="157"></a>157  
 Virginia Vassilevska Williams and Ryan Williams  
 Subcubic equivalences between path, matrix, and triangle problems.  
 In 51st IEEE Symposium on Foundations of Computer Science (FOCS '10) pg. 645 - 654, 2010.

<a id="158"></a>158  
 Ben W. Reichardt  
 Reflections for quantum query algorithms.  
 In Proceedings of the 22nd ACM-SIAM Symposium on Discrete Algorithms (SODA), pg. 560-569, 2011.  
 [arXiv:1005.1601](https://arXiv.org/abs/1005.1601)

<a id="159"></a>159  
 Ben W. Reichardt  
 Span-program-based quantum algorithm for evaluating unbalanced formulas.  
 [arXiv:0907.1622](https://arXiv.org/abs/0907.1622), 2009.

<a id="160"></a>160  
 Ben W. Reichardt  
 Faster quantum algorithm for evaluating game trees.  
 In Proceedings of the 22nd ACM-SIAM Symposium on Discrete Algorithms (SODA), pg. 546-559, 2011.  
 [arXiv:0907.1623](https://arXiv.org/abs/0907.1623)

<a id="161"></a>161  
 Stacey Jeffery, Robin Kothari, and Frédéric Magniez  
 Improving quantum query complexity of Boolean matrix multiplication using graph collision.  
 In Proceedings of ICALP 2012, pg. 522-532.  
 [arXiv:1112.5855](https://arXiv.org/abs/1112.5855).

<a id="162"></a>162  
 Andrew M. Childs and Jason M. Eisenberg  
 Quantum algorithms for subset finding.  
 Quantum Information and Computation 5(7):593-604, 2005.  
 [arXiv:quant-ph/0311038](https://arXiv.org/abs/quant-ph/0311038).

<a id="163"></a>163  
 Aleksandrs Belovs and Robert Špalek  
 Adversary lower bound for the k-sum problem.  
 In Proceedings of ITCS 2013, pg. 323-328.  
 [arXiv:1206.6528](https://arXiv.org/abs/1206.6528).

<a id="164"></a>164  
 Bohua Zhan, Shelby Kimmel, and Avinatan Hassidim  
 Super-polynomial quantum speed-ups for Boolean evaluation trees with hidden structure.  
 ITCS 2012: Proceedings of the 3rd Innovations in Theoretical Computer Science, ACM, pg. 249-265.  
 [arXiv:1101.0796](https://arXiv.org/abs/1101.0796)

<a id="165"></a>165  
 Shelby Kimmel  
 Quantum adversary (upper) bound.  
 39th International Colloquium on Automata, Languages and Programming - ICALP 2012 Volume 7391, p. 557-568.  
 [arXiv:1101.0797](https://arXiv.org/abs/1101.0797)

<a id="166"></a>166  
 Stephen Jordan, Keith Lee, and John Preskill  
 Quantum algorithms for quantum field theories.  
 Science, Vol. 336, pg. 1130-1133, 2012.  
 [arXiv:1111.3633](https://arXiv.org/abs/1111.3633)

<a id="167"></a>167  
 Andris Ambainis and Ashley Montanaro  
 Quantum algorithms for search with wildcards and combinatorial group testing.  
 [arXiv:1210.1148](https://arXiv.org/abs/1210.1148), 2012.

<a id="168"></a>168  
 Andris Ambainis and Robert Špalek  
 Quantum algorithms for matching and network flows.  
 Proceedings of STACS 2007, pg. 172-183.  
 [arXiv:quant-ph/0508205](https://arXiv.org/abs/quant-ph/0508205)

<a id="169"></a>169  
 Nathan Wiebe, Daniel Braun, and Seth Lloyd  
 Quantum data-fitting.  
 Physical Review Letters 109, 050505, 2012.  
 [arXiv:1204.5242](https://arXiv.org/abs/1204.5242)

<a id="170"></a>170  
 Andrew Childs and Nathan Wiebe  
 Hamiltonian simulation using linear combinations of unitary operations.  
 Quantum Information and Computation 12, 901-924, 2012.  
 [arXiv:1202.5822](https://arXiv.org/abs/1202.5822)

<a id="171"></a>171  
 Stacey Jeffery, Robin Kothari, and Frédéric Magniez  
 Nested quantum walks with quantum data structures.  
 In Proceedings of the 24th ACM-SIAM Symposium on Discrete Algorithms (SODA'13), pg. 1474-1485, 2013.  
 [arXiv:1210.1199](https://arXiv.org/abs/1210.1199)

<a id="172"></a>172  
 Aleksandrs Belovs  
 Learning-graph-based quantum algorithm for k-distinctness.  
 Proceedings of STOC 2012, pg. 77-84.  
 [arXiv:1205.1534](https://arXiv.org/abs/1205.1534), 2012.

<a id="173"></a>173  
 Andrew Childs, Stacey Jeffery, Robin Kothari, and Frédéric Magniez  
 A time-efficient quantum walk for 3-distinctness using nested updates.  
 [arXiv:1302.7316](https://arXiv.org/abs/1302.7316), 2013.

<a id="174"></a>174  
 Hari Krovi and Alexander Russell  
 Quantum Fourier transforms and the complexity of link invariants for quantum doubles of finite groups.  
 Commun. Math. Phys. 334, 743-777, 2015  
 [arXiv:1210.1550](https://arXiv.org/abs/1210.1550)

<a id="175"></a>175  
 Troy Lee, Frédéric Magniez, and Miklos Santha  
 Improved quantum query algorithms for triangle finding and associativity testing.  
 [arXiv:1210.1014](https://arXiv.org/abs/1210.1014), 2012.

<a id="176"></a>176  
 Silvano Garnerone, Paolo Zanardi, and Daniel A. Lidar  
 Adiabatic quantum algorithm for search engine ranking.  
 Physical Review Letters 108:230506, 2012.

<a id="177"></a>177  
 R. D. Somma, S. Boixo, H. Barnum, and E. Knill  
 Quantum simulations of classical annealing.  
 Physical Review Letters 101:130504, 2008.  
 [arXiv:0804.1571](https://arXiv.org/abs/0804.1571)

<a id="178"></a>178  
 Daniel J. Bernstein, Stacey Jeffery, Tanja Lange, and Alexander Meurer  
 Quantum algorithms for the subset-sum problem.  
 from cr.yp.to.

<a id="179"></a>179  
 Boris Altshuler, Hari Krovi, and Jérémie Roland  
 Anderson localization casts clouds over adiabatic quantum optimization.  
 Proceedings of the National Academy of Sciences 107(28):12446-12450, 2010.  
 [arXiv:0912.0746](https://arXiv.org/abs/0912.0746)

<a id="180"></a>180  
 Ben Reichardt  
 The quantum adiabatic optimization algorithm and local minima.  
 In Proceedings of STOC 2004, pg. 502-510. [Erratum].

<a id="181"></a>181  
 Edward Farhi, Jeffrey Goldstone, and Sam Gutmann  
 Quantum adiabatic evolution algorithms versus simulated annealing.  
 [arXiv:quant-ph/0201031](https://arXiv.org/abs/quant-ph/0201031), 2002.

<a id="182"></a>182  
 E. Farhi, J. Goldstone, D. Gosset, S. Gutmann, H. B. Meyer, and P. Shor  
 Quantum adiabatic algorithms, small gaps, and different paths.  
 Quantum Information and Computation, 11(3/4):181-214, 2011.  
 [arXiv:0909.4766](https://arXiv.org/abs/0909.4766).

<a id="183"></a>183  
 Sergey Bravyi, David P. DiVincenzo, Roberto I. Oliveira, and Barbara M. Terhal  
 The Complexity of Stoquastic Local Hamiltonian Problems.  
 Quantum Information and Computation, 8(5):361-385, 2008.  
 [arXiv:quant-ph/0606140](https://arXiv.org/abs/quant-ph/0606140).

<a id="184"></a>184  
 Rolando D. Somma and Sergio Boixo  
 Spectral gap amplification.  
 SIAM Journal on Computing, 42:593-610, 2013.  
 [arXiv:1110.2494](https://arXiv.org/abs/1110.2494).

<a id="185"></a>185  
 Sabine Jansen, Mary-Beth Ruskai, Ruedi Seiler  
 Bounds for the adiabatic approximation with applications to quantum computation.  
 Journal of Mathematical Physics, 48:102111, 2007.  
 [arXiv:quant-ph/0603175](https://arXiv.org/abs/quant-ph/0603175).

<a id="186"></a>186  
 E. Farhi, J. Goldstone, S. Gutmann, J. Lapan, A. Lundgren, and D. Preda  
 A Quantum Adiabatic Evolution Algorithm Applied to Random Instances of an NP-Complete Problem.  
 Science, 292(5516):472-475, 2001.  
 [arXiv:quant-ph/0104129](https://arXiv.org/abs/quant-ph/0104129).

<a id="187"></a>187  
 Edward Farhi, Jeffrey Goldstone, Sam Gutmann, and Daniel Nagaj  
 How to make the quantum adiabatic algorithm fail.  
 International Journal of Quantum Information, 6(3):503-516, 2008.  
 [arXiv:quant-ph/0512159](https://arXiv.org/abs/quant-ph/0512159).

<a id="188"></a>188  
 Edward Farhi, Jeffrey Goldstone, Sam Gutmann, and Daniel Nagaj  
 Unstructured randomness, small gaps, and localization.  
 Quantum Information and Computation, 11(9/10):840-854, 2011.  
 [arXiv:1010.0009](https://arXiv.org/abs/1010.0009).

<a id="189"></a>189  
 Edward Farhi, Jeffrey Goldstone, Sam Gutmann  
 Quantum adiabatic evolution algorithms with different paths.  
 [arXiv:quant-ph/0208135](https://arXiv.org/abs/quant-ph/0208135), 2002.

<a id="190"></a>190  
 Wim van Dam, Michele Mosca, and Umesh Vazirani  
 How powerful is adiabatic quantum computation?  
 In Proceedings of FOCS 2001, pg. 279-287.  
 [arXiv:quant-ph/0206003](https://arXiv.org/abs/quant-ph/0206003) [See also this.]

<a id="191"></a>191  
 E. Farhi, D. Gosset, I. Hen, A. W. Sandvik, P. Shor, A. P. Young, and F. Zamponi  
 The performance of the quantum adiabatic algorithm on random instances of two optimization problems on regular hypergraphs.  
 Physical Review A, 86:052334, 2012.  
 [arXiv:1208.3757](https://arXiv.org/abs/1208.3757).

<a id="192"></a>192  
 Kristen L. Pudenz and Daniel A. Lidar  
 Quantum adiabatic machine learning.  
 Quantum Information Processing, 12:2027, 2013.  
 [arXiv:1109.0325](https://arXiv.org/abs/1109.0325).

<a id="193"></a>193  
 Frank Gaitan and Lane Clark  
 Ramsey numbers and adiabatic quantum computing.  
 Physical Review Letters, 108:010501, 2012.  
 [arXiv:1103.1345](https://arXiv.org/abs/1103.1345).

<a id="194"></a>194  
 Frank Gaitan and Lane Clark  
 Graph isomorphism and adiabatic quantum computing.  
 Physical Review A, 89(2):022342, 2014.  
 [arXiv:1304.5773](https://arXiv.org/abs/1304.5773), 2013.

<a id="195"></a>195  
 Hartmut Neven, Vasil S. Denchev, Geordie Rose, and William G. Macready  
 Training a binary classifier with the quantum adiabatic algorithm.  
 [arXiv:0811.0416](https://arXiv.org/abs/0811.0416), 2008.

<a id="196"></a>196  
 Robert Beals  
 Quantum computation of Fourier transforms over symmetric groups.  
 In Proceedings of STOC 1997, pg. 48-53.

<a id="197"></a>197  
 Dave Bacon, Isaac L. Chuang, and Aram W. Harrow  
 The quantum Schur transform: I. efficient qudit circuits.  
 In Proceedings of SODA 2007, pg. 1235-1244.  
 [arXiv:quant-ph/0601001](https://arXiv.org/abs/quant-ph/0601001).

<a id="198"></a>198  
 S. Morita, H. Nishimori  
 Mathematical foundation of quantum annealing.  
 Journal of Methematical Physics, 49(12):125210, 2008.

<a id="199"></a>199  
 A. B. Finnila, M. A. Gomez, C. Sebenik, C. Stenson, J. D. Doll  
 Quantum annealing: a new method for minimizing multidimensional functions.  
 Chemical Physics Letters, 219:343-348, 1994.

<a id="200"></a>200  
 D. Gavinsky and T. Ito  
 A quantum query algorithm for the graph collision problem.  
 [arXiv:1204.1527](https://arXiv.org/abs/1204.1527), 2012.

<a id="201"></a>201  
 Andris Ambainis, Kaspars Balodis, Jānis Iraids, Raitis Ozols, and Juris Smotrovs  
 Parameterized quantum query complexity of graph collision.  
 [arXiv:1305.1021](https://arXiv.org/abs/1305.1021), 2013.

<a id="202"></a>202  
 Kevin C. Zatloukal  
 Classical and quantum algorithms for testing equivalence of group extensions.  
 [arXiv:1305.1327](https://arXiv.org/abs/1305.1327), 2013.

<a id="203"></a>203  
 Andrew Childs and Gábor Ivanyos  
 Quantum computation of discrete logarithms in semigroups.  
 [arXiv:1310.6238](https://arXiv.org/abs/1310.6238), 2013.

<a id="204"></a>204  
 Matan Banin and Boaz Tsaban  
 A reduction of semigroup DLP to classic DLP.  
 [arXiv:1310.7903](https://arXiv.org/abs/1310.7903), 2013.

<a id="205"></a>205  
 D. W. Berry, R. Cleve, and R. D. Somma  
 Exponential improvement in precision for Hamiltonian-evolution simulation.  
 [arXiv:1308.5424](https://arXiv.org/abs/1308.5424), 2013.

<a id="206"></a>206  
 François Le Gall and Harumichi Nishimura  
 Quantum algorithms for matrix products over semirings.  
 [arXiv:1310.3898](https://arXiv.org/abs/1310.3898), 2013.

<a id="207"></a>207  
 Nolan Wallach  
 A quantum polylog algorithm for non-normal maximal cyclic hidden subgroups in the affine group of a finite field.  
 [arXiv:1308.1415](https://arXiv.org/abs/1308.1415), 2013.

<a id="208"></a>208  
 Lov Grover  
 Fixed-point quantum search.  
 Phys. Rev. Lett. 95(15):150501, 2005.  
 [arXiv:quant-ph/0503205](https://arXiv.org/abs/quant-ph/0503205)

<a id="209"></a>209  
 Tathagat Tulsi, Lov Grover, and Apoorva Patel  
 A new algorithm for fixed point quantum search.  
 Quantum Information and Computation 6(6):483-494, 2005.  
 [arXiv:quant-ph/0505007](https://arXiv.org/abs/quant-ph/0505007)

<a id="210"></a>210  
 Guoming Wang  
 Quantum algorithms for approximating the effective resistances of electrical networks.  
 [arXiv:1311.1851](https://arXiv.org/abs/1311.1851)

<a id="211"></a>211  
 Dominic W. Berry, Andrew M. Childs, Richard Cleve, Robin Kothari, and Rolando D. Somma  
 Exponential improvement in precision for simulating sparse Hamiltonians  
 [arXiv:1312.1414](https://arXiv.org/abs/1312.1414)

<a id="212"></a>212  
 Thomas Decker, Peter Høyer, Gabor Ivanyos, and Miklos Santha  
 Polynomial time quantum algorithms for certain bivariate hidden polynomial problems  
 [arXiv:1305.1543](https://arXiv.org/abs/1305.1543)

<a id="213"></a>213  
 Kirsten Eisenträger, Sean Hallgren, Alexei Kitaev, and Fang Song  
 A quantum algorithm for computing the unit group of an arbitrary degree number field  
 In Proceedings of STOC 2014 pg. 293-302.

<a id="214"></a>214  
 Seth Lloyd, Masoud Mohseni, and Patrick Robentrost  
 Quantum algorithms for supervised and unsupervised machine learning  
 [arXiv:1307.0411](https://arXiv.org/abs/1307.0411)

<a id="215"></a>215  
 Ashley Montanaro  
 Quantum pattern matching fast on average  
 [arXiv:1408.1816](https://arXiv.org/abs/1408.1816)

<a id="216"></a>216  
 Charles H. Bennett, Ethan Bernstein, Gilles Brassard, and Umesh Vazirani  
 Strengths and weaknesses of quantum computing  
 SIAM J. Comput. 26(5):1524-1540, 1997  
 [arXiv:quant-ph/9701001](https://arXiv.org/abs/quant-ph/9701001)

<a id="217"></a>217  
 H. Ramesh and V. Vinay  
 String matching in $\widetilde{O}(\sqrt{n} + \sqrt{m})$ quantum time  
 Journal of Discrete Algorithms 1:103-110, 2003  
 [arXiv:quant-ph/0011049](https://arXiv.org/abs/quant-ph/0011049)

<a id="218"></a>218  
 Greg Kuperberg  
 Another subexponential-time quantum algorithm for the dihedral hidden subgroup problem  
 In Proceedings of TQC pg. 20-34, 2013  
 [arXiv:1112.3333](https://arXiv.org/abs/1112.3333)

<a id="219"></a>219  
 Peter Høyer, Jan Neerbek, and Yaoyun Shi  
 Quantum complexities of ordered searching, sorting, and element distinctness  
 In Proceedings of ICALP pg. 346-357, 2001  
 [arXiv:quant-ph/0102078](https://arXiv.org/abs/quant-ph/0102078)

<a id="220"></a>220  
 Amnon Ta-Shma  
 Inverting well conditioned matrices in quantum logspace  
 In Proceedings of STOC 2013 pg. 881-890.

<a id="221"></a>221  
 Nathan Wiebe, Ashish Kapoor, and Krysta Svore  
 Quantum deep learning  
 [arXiv:1412.3489](https://arXiv.org/abs/1412.3489)

<a id="222"></a>222  
 Seth Lloyd, Silvano Garnerone, and Paolo Zanardi  
 Quantum algorithms for topological and geometric analysis of big data  
 [arXiv:1408.3106](https://arXiv.org/abs/1408.3106)

<a id="223"></a>223  
 David A. Meyer and James Pommersheim  
 Single-query learning from abelian and non-abelian Hamming distance oracles  
 [arXiv:0912.0583](https://arXiv.org/abs/0912.0583)

<a id="224"></a>224  
 Markus Hunziker, David A. Meyer, Jihun Park, James Pommersheim, and Mitch Rothstein  
 The geometry of quantum learning  
 Quantum Information Processing 9:321-341, 2010.  
 [arXiv:quant-ph/0309059](https://arXiv.org/abs/quant-ph/0309059)

<a id="225"></a>225  
 Lawrence M. Ioannou and Michele Mosca  
 Limitations on some simple adiabatic quantum algorithms  
 International Journal of Quantum Information, 6(3):419-426, 2008.  
 [arXiv:quant-ph/0702241](https://arXiv.org/abs/quant-ph/0702241)

<a id="226"></a>226  
 Michael Jarret and Stephen P. Jordan  
 Adiabatic optimization without local minima  
 Quantum Information and Computation, 15(3/4):0181-0199, 2015.  
 [arXiv:1405.7552](https://arXiv.org/abs/1405.7552)

<a id="227"></a>227  
 Matthew B. Hastings, Dave Wecker, Bela Bauer, and Matthias Troyer  
 Improving quantum algorithms for quantum chemistry  
 Quantum Information and Computation, 15(1/2):0001-0021, 2015.  
 [arXiv:1403.1539](https://arXiv.org/abs/1403.1539)

<a id="228"></a>228  
 Stephen P. Jordan, Keith S. M. Lee, and John Preskill  
 Quantum simulation of scattering in scalar quantum field theories  
 Quantum Information and Computation, 14(11/12):1014-1080, 2014.  
 [arXiv:1112.4833](https://arXiv.org/abs/1112.4833)

<a id="229"></a>229  
 Stephen P. Jordan, Keith S. M. Lee, and John Preskill  
 Quantum algorithms for fermionic quantum field theories  
 [arXiv:1404.7115](https://arXiv.org/abs/1404.7115)

<a id="230"></a>230  
 Gavin K. Brennen, Peter Rohde, Barry C. Sanders, and Sukhi Singh  
 Multi-scale quantum simulation of quantum field theory using wavelets  
 [arXiv:1412.0750](https://arXiv.org/abs/1412.0750)

<a id="231"></a>231  
 Hefeng Wang, Sabre Kais, Alán Aspuru-Guzik, and Mark R. Hoffmann.  
 Quantum algorithm for obtaining the energy spectrum of molecular systems  
 Physical Chemistry Chemical Physics, 10(35):5388-5393, 2008.  
 [arXiv:0907.0854](https://arXiv.org/abs/0907.0854)

<a id="232"></a>232  
 Ivan Kassal and Alán Aspuru-Guzik  
 Quantum algorithm for molecular properties and geometry optimization  
 Journal of Chemical Physics, 131(22), 2009.  
 [arXiv:0908.1921](https://arXiv.org/abs/0908.1921)

<a id="233"></a>233  
 James D. Whitfield, Jacob Biamonte, and Alán Aspuru-Guzik  
 Simulation of electronic structure Hamiltonians using quantum computers  
 Molecular Physics, 109(5):735-750, 2011.  
 [arXiv:1001.3855](https://arXiv.org/abs/1001.3855)

<a id="234"></a>234  
 Borzu Toloui and Peter J. Love  
 Quantum algorithms for quantum chemistry based on the sparsity of the CI-matrix  
 [arXiv:1312.2529](https://arXiv.org/abs/1312.2529)

<a id="235"></a>235  
 James D. Whitfield  
 Spin-free quantum computational simulations and symmetry adapted states  
 Journal of Chemical Physics, 139(2):021105, 2013.  
 [arXiv:1306.1147](https://arXiv.org/abs/1306.1147)

<a id="236"></a>236  
 Andrew W. Cross, Graeme Smith, and John A. Smolin  
 Quantum learning robust to noise  
 [arXiv:1407.5088](https://arXiv.org/abs/1407.5088)

<a id="237"></a>237  
 Aram W. Harrow and David J. Rosenbaum  
 Uselessness for an oracle model with internal randomness  
 Quantum Information and Computation 14(7/8):608-624, 2014  
 [arXiv:1111.1462](https://arXiv.org/abs/1111.1462)

<a id="238"></a>238  
 Jon R. Grice and David A. Meyer  
 A quantum algorithm for Viterbi decoding of classical convolutional codes  
 [arXiv:1405.7479](https://arXiv.org/abs/1405.7479)

<a id="239"></a>239  
 Alexander Barg and Shiyu Zhou  
 A quantum decoding algorithm of the simplex code  
 Proceedings of the 36th Annual Allerton Conference, 1998  
 Available at author's homepage.

<a id="240"></a>240  
 Guoming Wang  
 Span-program-based quantum algorithm for tree detection  
 [arXiv:1309.7713](https://arXiv.org/abs/1309.7713), 2013.

<a id="241"></a>241  
 François Le Gall, Harumichi Nishimura, and Seiichiro Tani  
 Quantum algorithm for finding constant-sized sub-hypergraphs over 3-uniform hypergraphs  
 In Proceedings of COCOON, 2014. pg. 429-440  
 [arXiv:1310.4127](https://arXiv.org/abs/1310.4127)

<a id="242"></a>242  
 Edward Farhi, Jeffrey Goldstone, and Sam Gutmann  
 A quantum approximate optimization algorithm  
 [arXiv:1411.4028](https://arXiv.org/abs/1411.4028), 2014.

<a id="243"></a>243  
 Edward Farhi, Jeffrey Goldstone, and Sam Gutmann  
 A quantum approximate optimization algorithm applied to a bounded occurrence constraint problem  
 [arXiv:1412.6062](https://arXiv.org/abs/1412.6062), 2014.

<a id="244"></a>244  
 Dominic W. Berry, Andrew M. Childs, Richard Cleve, Robin Kothari, and Rolando D. Somma  
 Simulating Hamiltonian dynamics with a truncated Taylor series  
 [arXiv:1412.4687](https://arXiv.org/abs/1412.4687), 2014.

<a id="245"></a>245  
 Dominic W. Berry, Andrew M. Childs, and Robin Kothari  
 Hamiltonian simulation with nearly optimal dependence on all parameters  
 [arXiv:1501.01715](https://arXiv.org/abs/1501.01715), 2015.

<a id="246"></a>246  
 Scott Aaronson  
 Read the fine print  
 Nature Physics 11:291-293, 2015.

<a id="247"></a>247  
 Alexander Elgart and George A. Hagedorn  
 A note on the switching adiabatic theorem  
 Journal of Mathematical Physics 53(10):102202, 2012.  
 [arXiv:1204.2318](https://arXiv.org/abs/1204.2318)

<a id="248"></a>248  
 Daniel J. Bernstein, Johannes Buchmann, and Erik Dahmen, Eds.  
 Post-Quantum Cryptography  
 Springer, 2009.

<a id="249"></a>249  
 B. D. Clader, B. C. Jacobs, and C. R. Sprouse  
 Preconditioned quantum linear system algorithm  
 Phys. Rev. Lett. 110:250504, 2013.  
 [arXiv:1301.2340](https://arXiv.org/abs/1301.2340)

<a id="250"></a>250  
 S. Lloyd, M. Mohseni, and P. Rebentrost  
 Quantum principal component analysis  
 Nature Physics. 10(9):631, 2014.  
 [arXiv:1307.0401](https://arXiv.org/abs/1307.0401)

<a id="251"></a>251  
 Patrick Rebentrost, Masoud Mohseni, and Seth Lloyd  
 Quantum support vector machine for big data classification  
 Phys. Rev. Lett. 113, 130503, 2014.  
 [arXiv:1307.0471](https://arXiv.org/abs/1307.0471)

<a id="252"></a>252  
 J. M. Pollard  
 Theorems on factorization and primality testing  
 Proceedings of the Cambridge Philosophical Society. 76:521-228, 1974.

<a id="253"></a>253  
 L. Babai, R. Beals, and A. Seress  
 Polynomial-time theory of matrix groups  
 In Proceedings of STOC 2009, pg. 55-64.

<a id="254"></a>254  
 Neil J. Ross and Peter Selinger  
 Optimal ancilla-free Clifford+T approximations of z-rotations  
 [arXiv:1403.2975](https://arXiv.org/abs/1403.2975), 2014.

<a id="255"></a>255  
 L. A. B. Kowada, C. Lavor, R. Portugal, and C. M. H. de Figueiredo  
 A new quantum algorithm for solving the minimum searching problem  
 International Journal of Quantum Information, Vol. 6, No. 3, pg. 427-436, 2008.

<a id="256"></a>256  
 Sean Hallgren and Aram Harrow  
 Superpolynomial speedups based on almost any quantum circuit  
 Proceedings of ICALP 2008, pg. 782-795.  
 [arXiv:0805.0007](https://arXiv.org/abs/0805.0007)

<a id="257"></a>257  
 Fernando G.S.L. Brandao and Michal Horodecki  
 Exponential quantum speed-ups are generic  
 Quantum Information and Computation, Vol. 13, Pg. 0901, 2013  
 [arXiv:1010.3654](https://arXiv.org/abs/1010.3654)

<a id="258"></a>258  
 Scott Aaronson and Andris Ambainis  
 Forrelation: A problem that optimally separates quantum from classical computing.  
 [arXiv:1411.5729](https://arXiv.org/abs/1411.5729), 2014.

<a id="259"></a>259  
 Z. Gedik  
 Computational speedup with a single qutrit  
 [arXiv:1403.5861](https://arXiv.org/abs/1403.5861), 2014.

<a id="260"></a>260  
 Boaz Barak, Ankur Moitra, Ryan O'Donnell, Prasad Raghavendra, Oded Regev, David Steurer, Luca Trevisan, Aravindan Vijayaraghavan, David Witmer, and John Wright  
 Beating the random assignment on constraint satisfaction problems of bounded degree  
 [arXiv:1505.03424](https://arXiv.org/abs/1505.03424), 2015.

<a id="261"></a>261  
 David Cornwell  
 Amplified Quantum Transforms  
 [arXiv:1406.0190](https://arXiv.org/abs/1406.0190), 2015.

<a id="262"></a>262  
 T. Laarhoven, M. Mosca, and J. van de Pol  
 Solving the shortest vector problem in lattices faster using quantum search  
 Proceedings of PQCrypto13, pp. 83-101, 2013.  
 [arXiv:1301.6176](https://arXiv.org/abs/1301.6176)

<a id="263"></a>263  
 Andrew M. Childs, Robin Kothari, and Rolando D. Somma  
 Quantum linear systems algorithm with exponentially improved dependence on precision  
 [arXiv:1511.02306](https://arXiv.org/abs/1511.02306), 2015.

<a id="264"></a>264  
 Ashley Montanaro  
 Quantum walk speedup of backtracking algorithms  
 [arXiv:1509.02374](https://arXiv.org/abs/1509.02374), 2015.

<a id="265"></a>265  
 Ashley Montanaro  
 Quantum speedup of Monte Carlo methods  
 [arXiv:1504.06987](https://arXiv.org/abs/1504.06987), 2015.

<a id="266"></a>266  
 Andris Ambainis, Aleksandrs Belovs, Oded Regev, and Ronald de Wolf  
 Efficient quantum algorithms for (gapped) group testing and junta testing  
 [arXiv:1507.03126](https://arXiv.org/abs/1507.03126), 2015.

<a id="267"></a>267  
 A. Atici and R. A. Servedio  
 Quantum algorithms for learning and testing juntas  
 Quantum Information Processing, 6(5):323-348, 2007.  
 [arXiv:0707.3479](https://arXiv.org/abs/0707.3479)

<a id="268"></a>268  
 Aleksandrs Belovs  
 Quantum algorithms for learning symmetric juntas via the adversary bound  
 Computational Complexity, 24(2):255-293, 2015.  
 (Also appears in proceedings of CCC'14).  
 [arXiv:1311.6777](https://arXiv.org/abs/1311.6777)

<a id="269"></a>269  
 Stacey Jeffery and Shelby Kimmel  
 NAND-trees, average choice complexity, and effective resistance  
 [arXiv:1511.02235](https://arXiv.org/abs/1511.02235), 2015.

<a id="270"></a>270  
 Scott Aaronson, Shalev Ben-David, and Robin Kothari  
 Separations in query complexity using cheat sheets  
 [arXiv:1511.01937](https://arXiv.org/abs/1511.01937), 2015.

<a id="271"></a>271  
 Frédéric Grosshans, Thomas Lawson, François Morain, and Benjamin Smith  
 Factoring safe semiprimes with a single quantum query  
 [arXiv:1511.04385](https://arXiv.org/abs/1511.04385), 2015.

<a id="272"></a>272  
 Agnis Āriņš  
 Span-program-based quantum algorithms for graph bipartiteness and connectivity  
 [arXiv:1510.07825](https://arXiv.org/abs/1510.07825), 2015.

<a id="273"></a>273  
 Juan Bermejo-Vega and Kevin C. Zatloukal  
 Abelian hypergroups and quantum computation  
 [arXiv:1509.05806](https://arXiv.org/abs/1509.05806), 2015.

<a id="274"></a>274  
 Andrew Childs and Jeffrey Goldstone  
 Spatial search by quantum walk  
 Physical Review A, 70:022314, 2004.  
 [arXiv:quant-ph/0306054](https://arXiv.org/abs/quant-ph/0306054)

<a id="275"></a>275  
 Shantanav Chakraborty, Leonardo Novo, Andris Ambainis, and Yasser Omar  
 Spatial search by quantum walk is optimal for almost all graphs  
 [arXiv:1508.01327](https://arXiv.org/abs/1508.01327), 2015.

<a id="276"></a>276  
 François Le Gall  
 Improved quantum algorithm for triangle finding via combinatorial arguments  
 In Proceedings of the 55th IEEE Annual Symposium on Foundations of Computer Science (FOCS), pg. 216-225, 2014.  
 [arXiv:1407.0085](https://arXiv.org/abs/1407.0085)

<a id="277"></a>277  
 Ashley Montanaro  
 The quantum complexity of approximating the frequency moments  
 [arXiv:1505.00113](https://arXiv.org/abs/1505.00113), 2015.

<a id="278"></a>278  
 Rolando D. Somma  
 Quantum simulations of one dimensional quantum systems  
 [arXiv:1503.06319](https://arXiv.org/abs/1503.06319), 2015.

<a id="279"></a>279  
 Bill Fefferman and Cedric Yen-Yu Lin  
 A complete characterization of unitary quantum space  
 [arXiv:1604.01384](https://arXiv.org/abs/1604.01384), 2016.

<a id="280"></a>280  
 Tsuyoshi Ito and Stacey Jeffery  
 Approximate span programs  
 [arXiv:1507.00432](https://arXiv.org/abs/1507.00432), 2015.

<a id="281"></a>281  
 Arnau Riera, Christian Gogolin, and Jens Eisert  
 Thermalization in nature and on a quantum computer  
 Physical Review Letters, 108:080402 (2012)  
 [arXiv:1102.2389](https://arXiv.org/abs/1102.2389).

<a id="282"></a>282  
 Michael J. Kastoryano and Fernando G. S. L. Brandao  
 Quantum Gibbs Samplers: the commuting case  
 Communications in Mathematical Physics, 344(3):915-957 (2016)  
 [arXiv:1409.3435](https://arXiv.org/abs/1409.3435).

<a id="283"></a>283  
 Andrew M. Childs, David Jao, and Vladimir Soukharev  
 Constructing elliptic curve isogenies in quantum subexponential time  
 Journal of Mathematical Cryptology, 8(1):1-29 (2014)  
 [arXiv:1012.4019](https://arXiv.org/abs/1012.4019).

<a id="284"></a>284  
 Markus Grassl, Brandon Langenberg, Martin Roetteler, and Rainer Steinwandt  
 Applying Grover's algorithm to AES: quantum resource estimates  
 [arXiv:1512.04965](https://arXiv.org/abs/1512.04965), 2015.

<a id="285"></a>285  
 M. Ami, O. Di Matteo, V. Gheorghiu, M. Mosca, A. Parent, and J. Schanck  
 Estimating the cost of generic quantum pre-image attacks on SHA-2 and SHA-3  
 [arXiv:1603.09383](https://arXiv.org/abs/1603.09383), 2016.

<a id="286"></a>286  
 Marc Kaplan, Gaetan Leurent, Anthony Leverrier, and Maria Naya-Plasencia  
 Quantum differential and linear cryptanalysis  
 [arXiv:1510.05836](https://arXiv.org/abs/1510.05836), 2015.

<a id="287"></a>287  
 Scott Fluhrer  
 Quantum Cryptanalysis of NTRU  
 Cryptology ePrint Archive: Report 2015/676, 2015.

<a id="288"></a>288  
 Marc Kaplan  
 Quantum attacks against iterated block ciphers  
 [arXiv:1410.1434](https://arXiv.org/abs/1410.1434), 2014.

<a id="289"></a>289  
 H. Kuwakado and M. Morii  
 Quantum distinguisher between the 3-round Feistel cipher and the random permutation  
 In Proceedings of IEEE International Symposium on Information Theory (ISIT), pg. 2682-2685, 2010.

<a id="290"></a>290  
 H. Kuwakado and M. Morii  
 Security on the quantum-type Even-Mansour cipher  
 In Proceedings of International Symposium on Information Theory and its Applications (ISITA), pg. 312-316, 2012.

<a id="291"></a>291  
 Martin Roetteler and Rainer Steinwandt  
 A note on quantum related-key attacks  
 [arXiv:1306.2301](https://arXiv.org/abs/1306.2301), 2013.

<a id="292"></a>292  
 Thomas Santoli and Christian Schaffner  
 Using Simon's algorithm to attack symmetric-key cryptographic primitives  
 [arXiv:1603.07856](https://arXiv.org/abs/1603.07856), 2016.

<a id="293"></a>293  
 Rolando D. Somma  
 A Trotter-Suzuki approximation for Lie groups with applications to Hamiltonian simulation  
 [arXiv:1512.03416](https://arXiv.org/abs/1512.03416), 2015.

<a id="294"></a>294  
 Guang Hao Low and Isaac Chuang  
 Optimal Hamiltonian simulation by quantum signal processing  
 [arXiv:1606.02685](https://arXiv.org/abs/1606.02685), 2016.

<a id="295"></a>295  
 Dominic W. Berry and Leonardo Novo  
 Corrected quantum walk for optimal Hamiltonian simulation  
 [arXiv:1606.03443](https://arXiv.org/abs/1606.03443), 2016.

<a id="296"></a>296  
 Ashley Montanaro and Sam Pallister  
 Quantum algorithms and the finite element method  
 [arXiv:1512.05903](https://arXiv.org/abs/1512.05903), 2015.

<a id="297"></a>297  
 Lin-Chun Wan, Chao-Hua Yu, Shi-Jie Pan, Fei Gao, and Qiao-Yan Wen  
 Quantum algorithm for the Toeplitz systems  
 [arXiv:1608.02184](https://arXiv.org/abs/1608.02184), 2016.

<a id="298"></a>298  
 Salvatore Mandra, Gian Giacomo Guerreschi, and Alan Aspuru-Guzik  
 Faster than classical quantum algorithm for dense formulas of exact satisfiability and occupation problems  
 [arXiv:1512.00859](https://arXiv.org/abs/1512.00859), 2015.

<a id="299"></a>299  
 J. Adcock, E. Allen, M. Day, S. Frick, J. Hinchliff, M. Johnson, S. Morley-Short, S. Pallister, A. Price, and S. Stanisic  
 Advances in quantum machine learning  
 [arXiv:1512.02900](https://arXiv.org/abs/1512.02900), 2015.

<a id="300"></a>300  
 Cedric Yen-Yu Lin and Yechao Zhu  
 Performance of QAOA on typical instances of constraint satisfaction problems with bounded degree  
 [arXiv:1601.01744](https://arXiv.org/abs/1601.01744), 2016.

<a id="301"></a>301  
 Dave Wecker, Matthew B. Hastings, and Matthias Troyer  
 Training a quantum optimizer  
 [arXiv:1605.05370](https://arXiv.org/abs/1605.05370), 2016.

<a id="302"></a>302  
 Edward Farhi and Aram W. Harrow  
 Quantum supremacy through the quantum approximate optimization algorithm  
 [arXiv:1602.07674](https://arXiv.org/abs/1602.07674), 2016.

<a id="303"></a>303  
 Thomas G. Wong  
 Quantum walk search on Johnson graphs  
 [arXiv:1601.04212](https://arXiv.org/abs/1601.04212), 2016.

<a id="304"></a>304  
 Jonatan Janmark, David A. Meyer, and Thomas G. Wong  
 Global symmetry is unnecessary for fast quantum search  
 Physical Review Letters 112:210502, 2014.  
 [arXiv:1403.2228](https://arXiv.org/abs/1403.2228)

<a id="305"></a>305  
 David A. Meyer and Thomas G. Wong  
 Connectivity is a poor indicator of fast quantum search  
 Physical Review Letters 114:110503, 2014.  
 [arXiv:1409.5876](https://arXiv.org/abs/1409.5876)

<a id="306"></a>306  
 Thomas G. Wong  
 Spatial search by continuous-time quantum walk with multiple marked vertices  
 Quantum Information Processing 15(4):1411-1443, 2016.  
 [arXiv:1501.07071](https://arXiv.org/abs/1501.07071)

<a id="307"></a>307  
 Anirban Naryan Chowdhury and Rolando D. Somma  
 Quantum algorithms for Gibbs sampling and hitting-time estimation  
 [arXiv:1603.02940](https://arXiv.org/abs/1603.02940), 2016.

<a id="308"></a>308  
 Edward Farhi, Shelby Kimmel, and Kristan Temme  
 A quantum version of Schoning's algorithm applied to quantum 2-SAT  
 [arXiv:1603.06985](https://arXiv.org/abs/1603.06985), 2016.

<a id="309"></a>309  
 Iordanis Kerenidis and Anupam Prakash  
 Quantum recommendation systems  
 [arXiv:1603.08675](https://arXiv.org/abs/1603.08675), 2016.

<a id="310"></a>310  
 Markus Reiher, Nathan Wiebe, Krysta M. Svore, Dave Wecker, and Matthias Troyer  
 Elucidating reaction mechanisms on quantum computers  
 [arXiv:1605.03590](https://arXiv.org/abs/1605.03590), 2016.

<a id="311"></a>311  
 Aram W. Harrow and Ashley Montanaro  
 Sequential measurements, disturbance, and property testing  
 [arXiv:1607.03236](https://arXiv.org/abs/1607.03236), 2016.

<a id="312"></a>312  
 Martin Roetteler  
 Quantum algorithms for abelian difference sets and applications to dihedral hidden subgroups  
 [arXiv:1608.02005](https://arXiv.org/abs/1608.02005), 2016.

<a id="313"></a>313  
 Fernando G.S.L. Brandao and Krysta Svore  
 Quantum speed-ups for semidefinite programming  
 [arXiv:1609.05537](https://arXiv.org/abs/1609.05537), 2016.

<a id="314"></a>314  
 Z-C Yang, A. Rahmani, A. Shabani, H. Neven, and C. Chamon  
 Optimizing variational quantum algorithms using Pontryagins's minimum principle  
 [arXiv:1607.06473](https://arXiv.org/abs/1607.06473), 2016.

<a id="315"></a>315  
 Gilles Brassard, Peter Høyer, and Alain Tapp  
 Quantum cryptanalysis of hash and claw-free functions  
 In Proceedings of the 3rd Latin American symposium on Theoretical Informatics (LATIN'98), pg. 163-169, 1998.

<a id="316"></a>316  
 Daniel J. Bernstein  
 Cost analysis of hash collisions: Will quantum computers make SHARCS obsolete?  
 In Proceedings of the 4th Workshop on Special-purpose Hardware for Attacking Cryptographic Systems (SHARCS'09), pg. 105-116, 2009.

<a id="317"></a>317  
 Chris Cade, Ashley Montanaro, and Aleksandrs Belovs  
 Time and space efficient quantum algorithms for detecting cycles and testing bipartiteness  
 [arXiv:1610.00581](https://arXiv.org/abs/1610.00581), 2016.

<a id="318"></a>318  
 A. Belovs and B. Reichardt  
 Span programs and quantum algorithms for st-connectivity and claw detection  
 In European Symposium on Algorithms (ESA'12) , pg. 193-204, 2012.  
 [arXiv:1203.2603](https://arXiv.org/abs/1203.2603)

<a id="319"></a>319  
 Titouan Carette, Mathieu Laurière, and Frédéric Magniez  
 Extended learning graphs for triangle finding  
 [arXiv:1609.07786](https://arXiv.org/abs/1609.07786), 2016.

<a id="320"></a>320  
 F. Le Gall and N. Shogo  
 Quantum algorithm for triangle finding in sparse graphs  
 In Proceedings of the 26th International Symposium on Algorithms and Computation (ISAAC'15), pg. 590-600, 2015.

<a id="321"></a>321  
 Or Sattath and Itai Arad  
 A constructive quantum Lovász local lemma for commuting projectors  
 Quantum Information and Computation, 15(11/12)987-996pg, 2015.  
 [arXiv:1310.7766](https://arXiv.org/abs/1310.7766)

<a id="322"></a>322  
 Martin Schwarz, Toby S. Cubitt, and Frank Verstraete  
 An information-theoretic proof of the constructive commutative quantum Lovász local lemma  
 [arXiv:1311.6474](https://arXiv.org/abs/1311.6474)

<a id="323"></a>323  
 C. Shoen, E. Solano, F. Verstraete, J. I. Cirac, and M. M. Wolf  
 Sequential generation of entangled multi-qubit states  
 Physical Review Letters, 95:110503, 2005.  
 [arXiv:quant-ph/0501096](https://arXiv.org/abs/quant-ph/0501096)

<a id="324"></a>324  
 C. Shoen, K. Hammerer, M. M. Wolf, J. I. Cirac, and E. Solano  
 Sequential generation of matrix-product states in cavity QED  
 Physical Review A, 75:032311, 2007.  
 [arXiv:quant-ph/0612101](https://arXiv.org/abs/quant-ph/0612101)

<a id="325"></a>325  
 Yimin Ge, András Molnár, and J. Ignacio Cirac  
 Rapid adiabatic preparation of injective PEPS and Gibbs states  
 Physical Review Letters, 116:080503, 2016.  
 [arXiv:1508.00570](https://arXiv.org/abs/1508.00570)

<a id="326"></a>326  
 Martin Schwarz, Kristan Temme, and Frank Verstraete  
 Preparing projected entangled pair states on a quantum computer  
 Physical Review Letters, 108:110502, 2012.  
 [arXiv:1104.1410](https://arXiv.org/abs/1104.1410)

<a id="327"></a>327  
 Martin Schwarz, Toby S. Cubitt, Kristan Temme, Frank Verstraete, and David Perez-Garcia  
 Preparing topological PEPS on a quantum computer  
 Physical Review A, 88:032321, 2013.  
 [arXiv:1211.4050](https://arXiv.org/abs/1211.4050)

<a id="328"></a>328  
 M. Schwarz, O. Buerschaper, and J. Eisert  
 Approximating local observables on projected entangled pair states  
 [arXiv:1606.06301](https://arXiv.org/abs/1606.06301), 2016.

<a id="329"></a>329  
 Jean-François Biasse and Fang Song  
 Efficient quantum algorithms for computing class groups and solving the principal ideal problem in arbitrary degree number fields  
 Proceedings of the 27th Annual ACM-SIAM Symposium on Discrete Algorithms (SODA '16), pg. 893-902, 2016.

<a id="330"></a>330  
 Peter Høyer and Mojtaba Komeili  
 Efficient quantum walk on the grid with multiple marked elements  
 Proceedings of the 34th Symposium on Theoretical Aspects of Computer Science (STACS 2017), 42, 2016.  
 [arXiv:1612.08958](https://arXiv.org/abs/1612.08958)

<a id="331"></a>331  
 Peter Wittek  
 Quantum Machine Learning: what quantum computing means to data mining  
 Academic Press, 2014.

<a id="332"></a>332  
 Maria Schuld, Ilya Sinayskiy, and Francesco Petruccione  
 An introduction to quantum machine learning  
 Contemporary Physics, 56(2):172, 2014.  
 [arXiv:1409.3097](https://arXiv.org/abs/1409.3097)

<a id="333"></a>333  
 J. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost, N. Wiebe, and S. Lloyd  
 Quantum machine learning  
 [arXiv:1611.09347](https://arXiv.org/abs/1611.09347)

<a id="334"></a>334  
 Esma Aïeur, Gilles Brassard, and Sébastien Gambs  
 Machine learning in a quantum world  
 In Advances in Artificial Intelligence: 19th Conference of the Canadian Society for Computational Studies of Intelligence pg. 431-442, Springer, 2006.

<a id="335"></a>335  
 Vedran Dunjko, Jacob Taylor, and Hans Briegel  
 Quantum-enhanced machine learning  
 Phys. Rev. Lett 117:130501, 2016.

<a id="336"></a>336  
 Nathan Wiebe, Ashish Kapoor, and Krysta Svore  
 Quantum algorithms for nearest-neighbor methods for supervised and unsupervised learning  
 Quantum Information and Computation 15(3/4): 0318-0358, 2015.  
 [arXiv:1401.2142](https://arXiv.org/abs/1401.2142)

<a id="337"></a>337  
 Seokwon Yoo, Jeongho Bang, Changhyoup Lee, and Junhyoug Lee  
 A quantum speedup in machine learning: finding a N-bit Boolean function for a classification  
 New Journal of Physics 6(10):103014, 2014.  
 [arXiv:1303.6055](https://arXiv.org/abs/1303.6055)

<a id="338"></a>338  
 Maria Schuld, Ilya Sinayskiy, and Frencesco Petruccione  
 Prediction by linear regression on a quantum computer  
 Physical Review A 94:022342, 2016.  
 [arXiv:1601.07823](https://arXiv.org/abs/1601.07823)

<a id="339"></a>339  
 Zhikuan Zhao, Jack K. Fitzsimons, and Joseph F. Fitzsimons  
 Quantum assisted Gaussian process regression  
 [arXiv:1512.03929](https://arXiv.org/abs/1512.03929)

<a id="340"></a>340  
 Esma Aïeur, Gilles Brassard, and Sébastien Gambs  
 Quantum speed-up for unsupervised learning  
 Machine Learning, 90(2):261-287, 2013.

<a id="341"></a>341  
 Nathan Wiebe, Ashish Kapoor, and Krysta Svore  
 Quantum perceptron models  
 Advances in Neural Information Processing Systems 29 (NIPS 2016), pg. 3999â4007, 2016.  
 [arXiv:1602.04799](https://arXiv.org/abs/1602.04799)

<a id="342"></a>342  
 G. Paparo, V. Dunjko, A. Makmal, M. Martin-Delgado, and H. Briegel  
 Quantum speedup for active learning agents  
 Physical Review X4(3):031002, 2014.  
 [arXiv:1401.4997](https://arXiv.org/abs/1401.4997)

<a id="343"></a>343  
 Daoyi Dong, Chunlin Chen, Hanxiong Li, and Tzyh-Jong Tarn  
 Quantum reinforcement learning  
 IEEE Transactions on Systems, Man, and Cybernetics- Part B (Cybernetics)38(5):1207, 2008.

<a id="344"></a>344  
 Daniel Crawford, Anna Levit, Navid Ghadermarzy, Jaspreet S. Oberoi, and Pooya Ronagh  
 Reinforcement learning using quantum Boltzmann machines  
 [arXiv:1612.05695](https://arXiv.org/abs/1612.05695), 2016.

<a id="345"></a>345  
 Steven H. Adachi and Maxwell P. Henderson  
 Application of Quantum Annealing to Training of Deep Neural Networks  
 [arXiv:1510.06356](https://arXiv.org/abs/1510.06356), 2015.

<a id="346"></a>346  
 M. Benedetti, J. Realpe-Gómez, R. Biswas, and A. Perdomo-Ortiz  
 Quantum-assisted learning of graphical models with arbitrary pairwise connectivity  
 [arXiv:1609.02542](https://arXiv.org/abs/1609.02542), 2016.

<a id="347"></a>347  
 M. Benedetti, J. Realpe-Gómez, R. Biswas, and A. Perdomo-Ortiz  
 Quantum-assisted learning of graphical models with arbitrary pairwise connectivity  
 [arXiv:1609.02542](https://arXiv.org/abs/1609.02542), 2016.

<a id="348"></a>348  
 M. H. Amin, E. Andriyash, J. Rolfe, B. Kulchytskyy, and R. Melko  
 Quantum Boltzmann machine  
 [arXiv:1601.02036](https://arXiv.org/abs/1601.02036), 2016.

<a id="349"></a>349  
 Peter Wittek and Christian Gogolin  
 Quantum enhanced inference in Markov logic networks  
 Scientific Reports7:45672, 2017.  
 [arXiv:1611.08104](https://arXiv.org/abs/1611.08104), 2016.

<a id="350"></a>350  
 N. H. Bshouty and J. C. Jackson  
 Learning DNF over the uniform distribution using a quantum example oracle  
 SIAM Journal on Computing28(3):1136-1153, 1999.

<a id="351"></a>351  
 Srinivasan Arunachalam and Ronald de Wolf  
 A survey of quantum learning theory  
 [arXiv:1701.06806](https://arXiv.org/abs/1701.06806), 2017.

<a id="352"></a>352  
 Rocco A. Servedio and Steven J. Gortler  
 Equivalences and separations between quantum and classical learnability  
 SIAM Journal on Computing, 33(5):1067-1092, 2017.

<a id="353"></a>353  
 Srinivasan Arunachalam and Ronald de Wolf  
 Optimal quantum sample complexity of learning algorithms  
 [arXiv:1607.00932](https://arXiv.org/abs/1607.00932), 2016.

<a id="354"></a>354  
 Alex Monràs, Gael Sentís, and Peter Wittek  
 Inductive quantum learning: why you are doing it almost right  
 [arXiv:1605.07541](https://arXiv.org/abs/1605.07541), 2016.

<a id="355"></a>355  
 A. Bisio, G. Chiribella, G. M. D'Ariano, S. Facchini, and P. Perinotti  
 Optimal quantum learning of a unitary transformation  
 Physical Review A 81:032324, 2010.  
 [arXiv:0903.0543](https://arXiv.org/abs/0903.0543).

<a id="356"></a>356  
 M. Sasaki, A. Carlini, and R. Jozsa  
 Quantum template matching  
 Physical Review A 64:022317, 2001.  
 [arXiv:quant-ph/0102020](https://arXiv.org/abs/quant-ph/0102020).

<a id="357"></a>357  
 Masahide Sasaki and Alberto Carlini  
 Quantum learning and universal quantum matching machine  
 Physical Review A 66:022303, 2002.  
 [arXiv:quant-ph/0202173](https://arXiv.org/abs/quant-ph/0202173).

<a id="358"></a>358  
 Esma Aïeur, Gilles Brassard, and Sébastien Gambs  
 Quantum clustering algorithms  
 In Proceedings of the 24th International Conference on Machine Learning (ICML), pg. 1-8, 2007.

<a id="359"></a>359  
 Iordanis Kerenidis and Anupam Prakash  
 Quantum gradient descent for linear systems and least squares  
 [arXiv:1704.04992](https://arXiv.org/abs/1704.04992), 2017.

<a id="360"></a>360  
 Dan Boneh and Mark Zhandry  
 Quantum-secure message authentication codes  
 In Proceedings of Eurocrypt, pg. 592-608, 2013.

<a id="361"></a>361  
 A. M. Childs, W. van Dam, S-H Hung, and I. E. Shparlinski  
 Optimal quantum algorithm for polynomial interpolation  
 In Proceedings of the 43rd International Colloquium on Automata, Languages, and Programming (ICALP), pg. 16:1-16:13, 2016.  
 [arXiv:1509.09271](https://arXiv.org/abs/1509.09271)

<a id="362"></a>362  
 Volker Strassen  
 Einige Resultate über Berechnungskomplexität  
 In Jahresbericht der Deutschen Mathematiker-Vereinigung, 78(1):1-8, 1976/1977.

<a id="363"></a>363  
 Stacey Jeffery  
 Frameworks for Quantum Algorithms  
 PhD thesis, U. Waterloo, 2014.

<a id="364"></a>364  
 Seiichiro Tani  
 An improved claw finding algorithm using quantum walk  
 In Mathematical Foundations of Computer Science (MFCS), pg. 536-547, 2007.  
 [arXiv:0708.2584](https://arXiv.org/abs/0708.2584)

<a id="365"></a>365  
 K. Iwama and A. Kawachi  
 A new quantum claw-finding algorithm for three functions  
 New Generation Computing, 21(4):319-327, 2003.

<a id="366"></a>366  
 D. J. Bernstein, N. Heninger, P. Lou, and L. Valenta  
 Post-quantum RSA  
 IACR e-print 2017/351, 2017.

<a id="367"></a>367  
 Francois Fillion-Gourdeau, Steve MacLean, and Raymond Laflamme  
 Quantum algorithm for the dsolution of the Dirac equation  
 [arXiv:1611.05484](https://arXiv.org/abs/1611.05484), 2016.

<a id="368"></a>368  
 Ali Hamed Moosavian and Stephen Jordan  
 Faster quantum algorithm to simulate Fermionic quantum field theory  
 [arXiv:1711.04006](https://arXiv.org/abs/1711.04006), 2017.

<a id="369"></a>369  
 Pedro C.S. Costa, Stephen Jordan, and Aaron Ostrander  
 Quantum algorithm for simulating the wave equation  
 [arXiv:1711.05394](https://arXiv.org/abs/1711.05394), 2017.

<a id="370"></a>370  
 Jeffrey Yepez  
 Highly covariant quantum lattice gas model of the Dirac equation  
 [arXiv:1106.0739](https://arXiv.org/abs/1106.0739), 2011.

<a id="371"></a>371  
 Jeffrey Yepez   
 Quantum lattice gas model of Dirac particles in 1+1 dimensions  
 [arXiv:1307.3595](https://arXiv.org/abs/1307.3595), 2013.

<a id="372"></a>372  
 Bruce M. Boghosian and Washington Taylor  
 Simulating quantum mechanics on a quantum computer  
 Physica D 120:30-42, 1998.  
 [[arXiv:quant-ph/9701019]](https://arXiv.org/abs/quant-ph/9701019)

<a id="373"></a>373  
 Yimin Ge, Jordi Tura, and J. Ignacio Cirac  
 Faster ground state preparation and high-precision ground  energy estimation on a quantum computer  
 [arXiv:1712.03193](https://arXiv.org/abs/1712.03193), 2017.

<a id="374"></a>374  
 Renato Portugal  
 Element distinctness revisited  
 [arXiv:1711.11336](https://arXiv.org/abs/1711.11336), 2017.

<a id="375"></a>375  
 Kanav Setia and James D. Whitfield  
 Bravyi-Kitaev superfast simulation of fermions on a quantum computer  
 [arXiv:1712.00446](https://arXiv.org/abs/1712.00446), 2017.

<a id="376"></a>376  
 Richard Cleve and Chunhao Wang  
 Efficient quantum algorithms for simulating Lindblad evolution  
 [arXiv:1612.09512](https://arXiv.org/abs/1612.09512), 2016.

<a id="377"></a>377  
 M. Kliesch, T. Barthel, C. Gogolin, M. Kastoryano, and J. Eisert  
 Dissipative quantum Church-Turing theorem  
 Physical Review Letters 107(12):120501, 2011.  
 [[arXiv:1105.3986]](https://arXiv.org/abs/1105.3986)

<a id="378"></a>378  
 A. M. Childs and T. Li  
 Efficient simulation of sparse Markovian quantum dynamics  
 [arXiv:1611.05543](https://arXiv.org/abs/1611.05543), 2016.

<a id="379"></a>379  
 R. Di Candia, J. S. Pedernales, A. del Campo, E. Solano, and J. Casanova  
 Quantum simulation of dissipative processes without reservoir engineering  
 Scientific Reports 5:9981, 2015.

<a id="380"></a>380  
 R. Babbush, D. Berry, M. Kieferová, G. H. Low, Y. Sanders, A. Sherer, and N. Wiebe  
 Improved techniques for preparing eigenstates of Fermionic Hamiltonians  
 [arXiv:1711.10460](https://arXiv.org/abs/1711.10460), 2017.

<a id="381"></a>381  
 D. Poulin, A. Kitaev, D. S. Steiger, M. B. Hasting, and M. Troyer  
 Fast quantum algorithm for spectral properties  
 [arXiv:1711.11025](https://arXiv.org/abs/1711.11025), 2017.

<a id="382"></a>382  
 Guang Hao Low and Isaac Chuang  
 Hamiltonian simulation bt qubitization  
 [arXiv:1610.06546](https://arXiv.org/abs/1610.06546), 2016.

<a id="383"></a>383  
 F.G.S.L. Brandão, A. Kalev, T. Li, C. Y.-Y. Lin, K. M. Svore, and X. Wu  
 Exponential quantum speed-ups for semidefinite programming with applications to quantum learning  
 [arXiv:1710.02581](https://arXiv.org/abs/1710.02581), 2017.

<a id="384"></a>384  
 M. Ekerå and J. Håstad  
 Quantum Algorithms for Computing Short Discrete Logarithms and Factoring RSA Integers  
 Proceedings of PQCrypto 2017, pg. 347-363. (LNCS Volume 10346), 2017.

<a id="385"></a>385  
 M. Ekerå
 On post-processing in the quantum algorithm for computing short discrete logarithms  
 IACR ePrint Archive Report 2017/1122, 2017.

<a id="386"></a>386  
 D. J. Bernstein, J.-F. Biasse, and M. Mosca  
 A low-resource quantum factoring algorithm  
 Proceedings of PQCrypto 2017, pg. 330-346 (LNCS Volume 10346), 2017.
